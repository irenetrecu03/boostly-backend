FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 'app' is the folder within the Docker container with all the application code
WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get install -y postgresql-client

RUN pip install --upgrade pip
RUN pip install -r requirements.txt


COPY entrypoint.sh .
RUN chmod +x /app/entrypoint.sh

# Copy files into the container
COPY . .

