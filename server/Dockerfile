FROM python:3.11-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

COPY server/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY server /app
COPY data /app/data

EXPOSE 8000

RUN python manage.py migrate --noinput

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "server.wsgi:application"]
