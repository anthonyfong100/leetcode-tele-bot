init:
	pipenv install -d

dev:
	uvicorn main:app --reload

prod:
	uvicorn main:app --host 0.0.0.0 --port 8888

test:
	pytest -v

coverage:
	pytest -v --cov=leetcode_tele_bot 

docker-build:
	docker build -t leetcode-tele-bot .

docker-dev: docker-build
	docker run --name leetcode-tele-bot -p 8888:8888 leetcode-tele-bot

docker-down:
	docker rm leetcode-tele-bot