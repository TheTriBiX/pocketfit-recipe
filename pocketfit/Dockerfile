# syntax=docker/dockerfile:1.4
FROM python:3.12-alpine AS builder
EXPOSE 8000
WORKDIR /app
COPY requirements.txt /app
RUN pip3 install -r requirements.txt --no-cache-dir
RUN pip3 install psycopg2-binary
COPY . /app
ENTRYPOINT ["python3"]
CMD ["manage.py", "grpcrunserver", "0.0.0.0:50051", "--dev"]