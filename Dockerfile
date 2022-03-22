FROM python:3.10.0

WORKDIR /app

COPY ./ /app/

RUN pip install -r ./requirements.txt

ENTRYPOINT ["sh", "entrypoint.sh"]