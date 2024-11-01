#!/bin/sh

# Exit on error
set -e

## Wait for PostgreSQL to start
#echo "Waiting for PostgreSQL..."
#while ! nc -z "$DB_HOST" "$DB_PORT"; do
#  sleep 0.1
#done
#echo "PostgreSQL started"

# Run migrations
echo "Running migrations..."
python manage.py makemigrations
python manage.py migrate

# Start the Django server
echo "Starting Django server..."
exec "$@"


