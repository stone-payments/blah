# Docker image
FROM python:3.5

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD ./requirements.txt /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt && \
    apt update && apt install libav-tools

# Make port 80 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "-u","./src/run.py"]
