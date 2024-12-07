FROM python:3.11-slim
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt ./

# Copy the current directory contents into the container at /app
COPY . /./

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app/project
# Expose port 8000 (Django default port)
EXPOSE 8000
# Set the default command to run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
