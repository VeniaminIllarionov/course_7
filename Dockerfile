FROM python:3

WORKDIR /app

COPY ./requirement.txt /app/

RUN pip install -r requirement.txt

COPY . /app/

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]