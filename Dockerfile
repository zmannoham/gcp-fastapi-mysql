# Use the official Python 3.10 image as the base image
FROM python:3.10

# Set environment variables for configuration
ENV PORT = 8080
ENV HOST = 0.0.0.0

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . /app

# Expose the port on which the application will run
EXPOSE 8080

# Set the entrypoint command to run uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
