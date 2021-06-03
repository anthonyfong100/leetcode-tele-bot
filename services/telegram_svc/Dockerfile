FROM python:slim

COPY ./dist/deps/*.whl ./
RUN pip install *.whl && rm -rf *.whl

COPY ./dist/*.whl ./
RUN pip install *.whl && rm -rf *.whl

CMD ["python", "-m", "telegram_svc.main"]
