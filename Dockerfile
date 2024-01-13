FROM python:3.11

WORKDIR /app

COPY . .

RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

RUN python manage.py collectstatic --noinput

CMD uwsgi --http=0.0.0.0:80 --module=backend.wsgi
