init:
	pipenv install -d

dev:
	python telebot_main.py --env dev

prod:
	python telebot_main.py --env prod

test:
	pipenv run pytest -s -v

coverage:
	pipenv run pytest -v --cov=./ tests/ --cov-report=xml

docker-build:
	docker build -t leetcode-tele-bot .

docker-dev: docker-build
	docker run --name leetcode-tele-bot -p 8888:8888 --env-file dev.env leetcode-tele-bot 

docker-down:
	docker rm leetcode-tele-bot