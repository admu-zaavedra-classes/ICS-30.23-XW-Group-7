# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /SearchEngine

# Copy the current directory contents into the container at /app
COPY . /SearchEngine/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 (Django default port)
EXPOSE 8000

# Set the environment variable to avoid python buffering issues
ENV PYTHONUNBUFFERED 1

# Set the default command to run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
