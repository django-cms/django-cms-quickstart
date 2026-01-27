FROM python:3.13

WORKDIR /app

RUN python -m pip install --upgrade pip

# optimizing the docker caching behaviour
COPY requirements.txt .
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY . .

RUN python manage.py collectstatic --noinput

CMD uvicorn backend.asgi:application --host=0.0.0.0 --port=80
