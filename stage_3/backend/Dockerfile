FROM python:3.12.13-alpine3.23

COPY ../stage_1/backend/requirements.txt /req.txt

RUN pip install --no-cache req.txt 

WORKDIR /app

COPY ../stage_1/backend/main.py /app/main.py

ENTRYPOINT ["python3", "main.py"]