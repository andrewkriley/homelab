# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install dependencies
RUN pip install --no-cache-dir flask

# Install netcat-traditional
RUN apt-get update && \
    apt-get install -y netcat-traditional && \
    rm -rf /var/lib/apt/lists/*

# Create working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY app.py /app/

# Expose the port the app runs on
EXPOSE 80

# Define the health check command
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD nc -z -w1 ${NFS_SERVER} ${NFS_PORT} || exit 1

# Run the application
CMD ["python", "app.py"]
EXPOSE 80
