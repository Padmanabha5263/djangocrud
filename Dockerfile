FROM python:3.10-slim

WORKDIR /app

COPY reqlock.txt /app/

RUN pip install --upgrade pip 
RUN pip install -r reqlock.txt

COPY . /app/

EXPOSE 8000

CMD ["python", "./djangocrud/manage.py", "runserver", "0.0.0.0:8000"]

