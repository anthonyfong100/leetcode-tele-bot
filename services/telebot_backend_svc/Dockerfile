FROM python:slim

COPY ./dist/deps/*.whl ./
RUN pip install *.whl && rm -rf *.whl

COPY ./dist/*.whl ./
RUN pip install *.whl && rm -rf *.whl

# CMD ["python", "-m", "telebot_backend_svc.main"]
CMD ["uvicorn", "telebot_backend_svc.main:app", "--host", "0.0.0.0", "--port", "8000"]