FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

ENV PYTHONPATH=/app/task_manager

CMD ["gunicorn", "task_manager.wsgi:application", "--bind", "0.0.0.0:8000"]
