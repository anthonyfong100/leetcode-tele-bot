_all: all
_clean: clean 

include ../../tools/Packages.mk


test:
	poetry run pytest -v --cov=./ tests/ --cov-report=xml
