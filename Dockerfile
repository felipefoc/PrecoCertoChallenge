FROM python:3.9-alpine

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt /requirements.txt

RUN python -m pip install -r requirements.txt

WORKDIR /app

COPY . /app

RUN ls

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]





