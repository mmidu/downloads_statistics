FROM python:3.7

COPY config/requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

WORKDIR /app/server

EXPOSE 8000

ENTRYPOINT ["uvicorn"]

CMD ["main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]

#CMD ["main:app", "--host", "0.0.0.0", "--port", "8000"]
