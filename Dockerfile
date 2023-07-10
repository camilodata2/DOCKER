FROM python:3.10.6-slim-buster

WORKDIR /app

COPY api/requariment.txt .

RUN pisp install  -U pip install -r requariment.txt

COPY api/ ./api

EXPOSE 8000

CMD [ "uvicorn","api.main:app --reload","0.0.0.0","--port","80" ]