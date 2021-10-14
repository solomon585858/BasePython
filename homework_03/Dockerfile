# To build docker image use:
# docker build -t homework_03 homework_03/

# To run docker container use:
# docker run -p 8000:8000 homework_03

FROM python:3.9-buster

WORKDIR /var/app

COPY blog/requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY blog .

EXPOSE 8000

CMD uvicorn app:app --host=0.0.0.0
