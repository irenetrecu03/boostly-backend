# Boostly App Backend

A brief description of the project and its purpose.

## Table of Contents

- [Project Setup](#project-setup)
- [Environment Variables](#environment-variables)
- [Running the Application](#running-the-application)
- [System Flow](#system-flow)
- [API Documentation](#api-documentation)
- [Testing](#testing)
- [Docker setup](#docker-setup)

---

## Project Setup

### Prerequisites

Ensure you have the following installed:

- [Python 3.8+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)
- [PostgreSQL](https://www.postgresql.org/download/) (or an alternative database if required)

### 1. Clone the Repository

```bash
git clone https://github.com/irenetrecu03/boostly-backend.git
cd your-repo
```

### 2. Set up a virtual environment

````bash
# Create a virtual environment
# On Windows:
python -m venv env
# On macOS/Linux:
python3 -m venv env

# Activate the virtual environment
# On Windows:
env\Scripts\activate
# On macOS/Linux:
source env/bin/activate
````

### 3. Install Dependencies
````bash
pip install -r requirements.txt
````

### 4. Set up the Database
Ensure PostgreSQL (or your chosen database) is running. Create a new database:
````bash
CREATE DATABASE boostly_db;
````
Update your environment variables to connect to the database (see [Environment Variables](#environment-variables)).

### 5. Run Migrations
````bash
python manage.py migrate
````

---

## Environment Variables
Create a .env file in the project root and configure the following variables:
````bash
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_NAME=your_database_name
DATABASE_USER=your_database_user
DATABASE_PASSWORD=your_database_password
DATABASE_HOST=localhost
DATABASE_PORT=5432
````
- SECRET_KEY: Set a unique Django secret key for your project.
- DEBUG: Set to `True` in development, `False` in production.
- DATABASE_NAME, DATABASE_USER, DATABASE_PASSWORD, DATABASE_HOST, DATABASE_PORT: Configure these with your database connection details.

---

## Running the Application
To start the server, run:
````bash
python manage.py runserver
````
The server should now be accessible at http://127.0.0.1:8000/.

If you are running Expo Go on another device, you need to expose the Django 
server over LAN:
````bash
python manage.py runserver 0.0.0.0:8000
````
Then create a tunnel using [ngrok](https://ngrok.com/):
````bash
ngrok http http://localhost:8000
````

For production, make sure to collect all static files:
````bash
python manage.py collectstatic
````

---

## System Flow

### 1. Creating a new User
The CustomUserManager is responsible for the creation of user instances at the database level. It contains methods 
like `create_user` and `create_superuser` that handle how users are created and saved.

The UserSerializer is designed for serializing and deserializing data when interacting with APIs. It validates incoming
data (e.g. checking that the password is provided) before creating a new user.

Here’s a simplified flow for creating a user through the serializer:

1. **API Request**: A POST request is made to create a new user.
2. **UserSerializer**: The serializer receives the data and validates it.
3. **Password Hashing**: The create method in UserSerializer hashes the password.
4. **Model Creation**: return `super(UserSerializer, self).create(validated_data)` calls ModelSerializer's `create` method:
   - This method instantiates the User model with the validated data.
   - It then calls the `save()` method of the User model.
5. **CustomUserManager**: The `save()` method utilizes the CustomUserManager for any custom logic (like password hashing), 
as defined in the CustomUserManager.

---

## API Documentation
Swagger/OpenAPI: http://127.0.0.1:8000/swagger/

---

## Testing
To run tests, use the following command:
````bash
python manage.py test
````

---

## Docker Setup
Build a docker image:
````bash
docker build -t boostly-backend-image .
````

Create a docker container with volumes:
````bash
docker run -d --name boostly-backend-container -v .:/app -p 8001:8000 boostly-backend-image
````

Run docker-compose.yml:
`````bash
docker compose up -d
`````
