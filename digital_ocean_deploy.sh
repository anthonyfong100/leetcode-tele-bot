#!/bin/bash

cd ~
wget https://github.com/digitalocean/doctl/releases/download/v1.60.0/doctl-1.60.0-linux-amd64.tar.gzdoctl auth init --access-token TOKEN_NAME
tar xf ~/doctl-1.60.0-linux-amd64.tar.gz
sudo mv ~/doctl /usr/local/bin


doctl registry login --expiry-seconds 180 --access-token TOKEN_NAME
docker pull registry.digitalocean.com/anthonyfong97/leetcode-tele-bot:latest

echo "starting server instance..."
docker run -d \
  --restart always \
  -p 0.0.0.0:80:80 \
  --name leetcode-tele-bot \
  registry.digitalocean.com/anthonyfong97/leetcode-tele-bot:latest
