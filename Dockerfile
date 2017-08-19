# Docker image
FROM python:3.5

# Set the working directory to /app
WORKDIR ./

# Copy the current directory contents into the container at /app
ADD . ./

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "/src/run.py"]

VOLUME [/Repos]