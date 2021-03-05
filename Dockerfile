FROM python:3.7-slim-buster

COPY ./tokenizers /user/local/nltk_data/tokenizers
COPY ./sentiment /user/local/nltk_data/sentiment

COPY ./requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

VOLUME ["/app"]
WORKDIR /app

EXPOSE 8501

ENTRYPOINT ["streamlit", "run"]

CMD ["app.py"]
