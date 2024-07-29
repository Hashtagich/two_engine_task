FROM python:3.9-slim

WORKDIR /usr/src/app

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

ENV PYTHONPATH=/app/task_management
ENV DJANGO_SETTINGS_MODULE=task_management.settings


#CMD ["gunicorn", "task_management.wsgi:application", "--bind", "0.0.0.0:8000", "--log-level", "info"]
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

CMD ["/entrypoint.sh"]