FROM python:3.9
LABEL authors="sangminlee"

RUN mkdir /code
WORKDIR /code
COPY . .

RUN pip install -r requirements.txt
WORKDIR app/src

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8501"]