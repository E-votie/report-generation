# Use an official Python runtime as a base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy application source code
COPY app/ ./app
COPY bot_data/ ./bot_data

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the .env file for environment variables
COPY .env ./app/.env

# Set the working directory to the app directory
WORKDIR /app/app

# Expose the port FastAPI will run on
EXPOSE 3001

# Command to run the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3001"]