FROM python:3.11-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /django

# Install system dependencies 
RUN apk update && apk add --no-cache \
    build-base \
    mariadb-dev \
    python3-dev \
    libstdc++ \
    alsa-lib-dev \
    portaudio-dev \
    libffi-dev

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Run migrate command
RUN python manage.py migrate --fake

# Run the tests
RUN python manage.py test --verbosity=2

# Expose the port for Django development server
EXPOSE 8000

# Default command to run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
