#!/bin/bash

sudo snap install doctl
doctl registry login --expiry-seconds 180
docker pull registry.digitalocean.com/anthonyfong97/leetcode-tele-bot:latest

echo "starting server instance..."
docker run -d \
  --restart always \
  -p 0.0.0.0:80:80 \
  --name leetcode-tele-bot \
  registry.digitalocean.com/anthonyfong97/leetcode-tele-bot:latest
