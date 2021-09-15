FROM python:3.8

RUN mkdir /app
WORKDIR /app

COPY ./src /app
COPY ./main.py /app/main.py
COPY ./requirements /app/requirements

RUN pip3 install --no-cache-dir -r requiremets

ENTRYPOINT ["python3", "main.py"]