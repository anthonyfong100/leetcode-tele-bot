#!/bin/bash


echo "Logging in into docker"
docker login -u DOCKER_USERNAME -p DOCKER_PASSWORD

echo "Pulling image"
docker pull anthonyfong/leetcode-tele-bot:latest

echo "starting telebot instance..."
docker run -d \
  --restart always \
  -p 0.0.0.0:80:80 \
  --name leetcode-tele-bot \
  --env TELEBOT_TOKEN=TELEBOT_TOKEN_VAL \
  anthonyfong/leetcode-tele-bot:latest


echo "starting telebot instance..."
docker run -d \
  --restart always \
  -p 0.0.0.0:8000:8000 \
  --name leetcode-server \
  --env TELEBOT_TOKEN=TELEBOT_TOKEN_VAL \
  anthonyfong/leetcode-server:latest
