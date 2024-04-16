FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install -r ./reqlock.txt

EXPOSE 8000

CMD ["python", "./djangocrud/manage.py", "runserver"]
