init:
	pipenv install -d

dev:
	uvicorn main:app --reload

prod:
	uvicorn main:app --host 0.0.0.0 --port 80

test:
	pytest -v

coverage:
	pytest -v --cov=leetcode_tele_bot 
