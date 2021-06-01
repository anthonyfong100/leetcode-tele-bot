#!/bin/bash


echo "Logging in into docker"
docker login -u DOCKER_USERNAME -p DOCKER_PASSWORD

echo "Pulling image"
docker pull anthonyfong/leetcode-tele-bot:latest

echo "starting server instance..."
docker run -d \
  --restart always \
  -p 0.0.0.0:80:80 \
  --name leetcode-tele-bot \
  anthonyfong/leetcode-tele-bot:latest
