# Boostly App Backend

A brief description of the project and its purpose.

## Table of Contents

- [Project Setup](#project-setup)
- [Environment Variables](#environment-variables)
- [Running the Application](#running-the-application)
- [API Documentation](#api-documentation)
- [Testing](#testing)

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

For production, make sure to collect all static files:
````bash
python manage.py collectstatic
````

---

## API Documentation
Swagger/OpenAPI: http://127.0.0.1:8000/swagger/

---

## Testing
To run tests, use the following command:
````bash
python manage.py test
````
