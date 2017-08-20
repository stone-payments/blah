# Docker image
FROM python:alpine

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD ./requirements.txt /app

# Install any needed packages specified in requirements.txt
RUN apk add --update ffmpeg python-dev build-base && \
pip install -r requirements.txt && \
rm -rf /var/cache/apk/*

# Make port 80 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "-u","./src/run.py"]
