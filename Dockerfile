# pull official base image
FROM python:3.8-alpine AS build-python
COPY ./requirements_prod.txt .
COPY ./requirements_base.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /wheels -r requirements_prod.txt

FROM python:3.8-alpine
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk del build-deps
COPY --from=build-python /wheels /wheels
COPY --from=build-python requirements_prod.txt .
RUN pip install --no-cache /wheels/*
WORKDIR /app
COPY . .
RUN python manage.py collectstatic --noinput

# add and run as non-root user
RUN adduser -D myuser
USER myuser

# run gunicorn
CMD gunicorn fortytwo_test_task.wsgi:application --bind 0.0.0.0:$PORT
