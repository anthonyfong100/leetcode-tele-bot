init:
	pipenv install -d

dev:
	python main.py --env dev

prod:
	python main.py --env prod

test:
	pipenv run pytest -s -v

coverage:
	pipenv run pytest -v --cov=leetcode_tele_bot tests/

docker-build:
	docker build -t leetcode-tele-bot .

docker-dev: docker-build
	docker run --name leetcode-tele-bot -p 8888:8888 leetcode-tele-bot

docker-down:
	docker rm leetcode-tele-bot