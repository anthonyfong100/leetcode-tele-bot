FROM python:3.7-slim

COPY Pipfile* /
RUN pip install pipenv
RUN pipenv lock -r > requirements.txt
RUN pip install -r /requirements.txt

COPY . ./leetcode-tele-bot-service
WORKDIR /leetcode-tele-bot-service
EXPOSE 8888

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8888"]