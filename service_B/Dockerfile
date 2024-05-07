FROM python:alpine3.10

WORKDIR /app

COPY . /app

RUN pip install Flask
EXPOSE 5100

CMD ["python", "launch.py"]
