FROM python:3.9-alpine

ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev mariadb-connector-c-dev

WORKDIR /django

COPY requirements.txt requirements.txt

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt -v

# Copy the entire project into the Docker image
COPY . .

# Run migrations and create a superuser
RUN python manage.py migrate

# Run Django migrations and create a superuser
# RUN python manage.py migrate
# RUN echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
