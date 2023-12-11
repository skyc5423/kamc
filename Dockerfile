FROM python:3.9
LABEL authors="sangminlee"

RUN mkdir /code
WORKDIR /code
COPY . .

RUN pip install -r requirements.txt
WORKDIR app/src

EXPOSE 8050

ENV PYTHONPATH "${PYTHONPATH}:/code"

ENTRYPOINT ["python", "main.py"]