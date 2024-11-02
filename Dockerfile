FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 'app' is the folder within the Docker container with all the application code
WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Install netcat
RUN apt-get update && apt-get install -y netcat-openbsd

COPY entrypoint.sh .
RUN chmod +x /app/entrypoint.sh

# Copy files into the container
COPY . .

# Expose the port Django runs on
EXPOSE 8000

# Set entry point
ENTRYPOINT ["/app/entrypoint.sh"]
# Run Django's development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
