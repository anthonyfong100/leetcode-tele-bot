_all: all
_clean: clean 

include ../../tools/Packages.mk


dev:
	poetry run uvicorn telebot_backend_svc.main:app --host 0.0.0.0 --port 8000