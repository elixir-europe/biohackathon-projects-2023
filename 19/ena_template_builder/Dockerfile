# Use Python Slim as the base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app/app

# Copy the requirements.txt to the container
COPY ./requirements.txt /app/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the Flask app code to the container
COPY . /app

# Expose the port that Flask will run on
EXPOSE 5000

# Command to run the application
CMD ["/app/run.sh"]
