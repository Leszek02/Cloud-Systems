FROM python:3.11-alpine3.19 as build 
# Additional libraries to build psycopg2 python package
RUN apk add build-base libpq libpq-dev

COPY stage_1/backend/requirements.txt ./

RUN pip3 install --no-cache-dir -r ./requirements.txt

WORKDIR /app

COPY stage_1/backend/main.py main.py

ENTRYPOINT ["python3", "main.py"]