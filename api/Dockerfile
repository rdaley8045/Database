FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7 as local
COPY --from=base /usr/src/app/. /usr/src/app/.
RUN  pip install --no-cache-dir -r /usr/src/app/requirements.txt
ENV PYTHONPATH "${PYTHONPATH}:/usr/src/app:/usr/src/app/api"
WORKDIR /usr/src/app/api
ENTRYPOINT uvicorn database:app --reload --port 5000 --host 0.0.0.0

ARG BUILD=dev
FROM local as dev
WORKDIR /usr/src/app/api
COPY . .
ENV PORT=5000
ENV VERSION=$BUILD
ENV CONFIG=prom.dev.json
ENTRYPOINT gunicorn -k uvicorn.workers.UvicornWorker -w 4 GWEX2:app

ARG BUILD=prod
FROM dev as prod
ENV CONFIG=prom.prod.json
