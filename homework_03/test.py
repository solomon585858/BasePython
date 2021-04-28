import asyncio
import aiohttp
import os

from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
)
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import (
    declarative_base,
    relationship,
    sessionmaker,
)

PG_CONN_URI = os.environ.get("PG_CONN_URI") or "postgresql+asyncpg://postgres:password@localhost/postgres"
engine = create_async_engine(PG_CONN_URI, echo=False)
Base = declarative_base()
Session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"

# users_data = []
# posts_data = []


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, default="", server_default="")
    username = Column(String, nullable=False, default="", server_default="")
    email = Column(String, nullable=False, default="", server_default="")

    posts = relationship("Post", back_populates="user")

    def __str__(self):
        return f"{self.__class__.__name__}" \
               f"(id={self.id}, name={self.name!r}, username={self.username!r}, email={self.email!r})"

    def __repr__(self):
        return str(self)


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    userId = Column(Integer, ForeignKey(User.id), nullable=False)
    title = Column(String, nullable=False, default="", server_default="")
    body = Column(String, nullable=False, default="", server_default="")

    user = relationship("User", back_populates="posts")

    def __str__(self):
        return f"{self.__class__.__name__}" \
               f"(id={self.id}, userId={self.userId}, title={self.title!r}, body={self.body!r})"

    def __repr__(self):
        return str(self)


async def create_tables():
    print(f"Creating tables for users and posts")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    print(f"Done creating tables for users and posts")


async def fetch_users():
    async with aiohttp.ClientSession() as session:
        print(f"Task Users getting data from URL: {USERS_DATA_URL}")
        async with session.get(USERS_DATA_URL) as response:
            user_data = await response.json()
            keys = ["name", "username", "email"]
            users_data = []
            for user in user_data:
                users_dict = {}
                for key, value in user.items():
                    if key in keys:
                        users_dict[key] = value
                users_data.append(users_dict)
            print(f"Task Users received all data from URL: {USERS_DATA_URL}")
            print(users_data)
            return users_data


async def fetch_posts():
    async with aiohttp.ClientSession() as session:
        print(f"Task Posts getting data from URL: {POSTS_DATA_URL}")
        async with session.get(POSTS_DATA_URL) as response:
            post_data = await response.json()
            keys = ["userId", "title", "body"]
            posts_data = []
            for post in post_data:
                posts_dict = {}
                for key, value in post.items():
                    if key in keys:
                        posts_dict[key] = value
                posts_data.append(posts_dict)
            print(f"Task Posts received all data from URL: {POSTS_DATA_URL}")
            print(posts_data)
            return posts_data


async def fill_users_table():
    print("Adding users to users table")
    async with Session() as session:
        session: AsyncSession

        async with session.begin():
            users = await fetch_users()
            for user_ in users:
                user_added = User(name=user_['name'], username=user_['username'], email=user_['email'])
                # print(f"Getting user: {user_added}")
                session.add(user_added)
    print("Done adding users to users table")


async def fill_posts_table():
    print("Adding posts to posts table")
    async with Session() as session:
        session: AsyncSession

        async with session.begin():
            posts = await fetch_posts()
            for post_ in posts:
                post_added = Post(userId=post_['userId'], title=post_['title'], body=post_['body'])
                # print(f"Getting post: {post_added}")
                session.add(post_added)
    print("Done adding posts to posts table")


async def async_main():
    await create_tables()
    # await asyncio.gather(
    #     asyncio.create_task(fetch_users()),
    #     asyncio.create_task(fetch_posts())
    # )
    await fill_users_table()
    await fill_posts_table()


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
