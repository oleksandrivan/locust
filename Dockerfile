# Use the official Python base image
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Locust files to the container
COPY locustfile.py .
COPY locustfile-proxy.py .
COPY run.sh .

# Expose the Locust web UI port
EXPOSE 8089

# Set the default command to run Locust
CMD ["sleep", "infinity"]
