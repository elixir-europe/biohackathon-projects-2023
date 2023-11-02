# Use Python Slim as the base image
FROM python:3.10-slim

RUN apt-get -y update
RUN apt-get install -y curl
RUN curl -sL https://deb.nodesource.com/setup_16.x -o nodesource_setup.sh
RUN bash nodesource_setup.sh
RUN apt-get install -y nodejs npm

# Set the working directory in the container
WORKDIR /app

# Copy the Flask app code to the container
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Expose the port the app will run on
EXPOSE 5173

# Command to run the application
CMD ["/app/run.sh"]
