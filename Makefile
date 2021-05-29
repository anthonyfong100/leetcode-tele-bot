init:
	pipenv install -d

dev:
	uvicorn main:app --reload

test:
	pytest -v

coverage:
	pytest -v --cov=leetcode_tele_bot 
