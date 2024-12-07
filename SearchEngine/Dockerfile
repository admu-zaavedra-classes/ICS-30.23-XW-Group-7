FROM python:3.11-slim
ENV PYTHONUNBUFFERED 1
ENV HOST 0.0.0.0

WORKDIR SearchEngine/
COPY requirements.txt ./

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Expose port 8000 (Django default port)
EXPOSE 8080
# Set the default command to run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]

