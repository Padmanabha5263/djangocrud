# djangocrud
create, read, update, delete operation using django rest framework

## Project setup
1. create virtual environment using python -m venv djangoRest command
2. install dependency using pip install -r ./reqlock.txt
3. cd ./djangocrud
4. run python manage.py runserver

## Docker image creation 
1. run docker build -t djangocrud .
2. run docker run --name dockercrudone -d -p 8000:8000 djangocrud
