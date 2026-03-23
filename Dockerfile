FROM python:3.5-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install --upgrade "pip<21" "setuptools<45" "wheel<0.35" && \
    pip install -r requirements.txt

COPY . /app

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
