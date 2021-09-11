"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import aiohttp

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


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
            return posts_data
