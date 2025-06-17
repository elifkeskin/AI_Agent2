# Use Python 3.11 slim image as base
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install build dependencies and pip
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install pip
RUN python -m pip install --no-cache-dir --upgrade pip

# Copy project files
COPY . .

# Install dependencies directly with pip
RUN pip install -e .

# Expose the port (assuming FastAPI default port)
EXPOSE 8000

# Command to run the application
ENTRYPOINT ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]