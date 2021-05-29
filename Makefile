init:
	pipenv install -d

test:
	pytest -v

coverage:
	pytest -v --cov=leetcode_tele_bot 
