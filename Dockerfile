FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY manage.py /app/manage.py
COPY nginx /app/nginx
COPY static /app/static
COPY static_root /app/static_root
COPY templates /app/templates
COPY schema.yml /app/schema.yml
COPY interview_management_system /app/interview_management_system