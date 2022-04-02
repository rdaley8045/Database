FROM python:3.9 as local

WORKDIR /usr/src/app/api

COPY requirements.txt .

RUN  pip3 install --no-cache-dir -r /usr/src/app/api/requirements.txt
ENV PYTHONPATH "${PYTHONPATH}:/usr/src/app:/usr/src/app/api"

ENTRYPOINT uvicorn mysql:app --reload --port 80 --host 0.0.0.0

