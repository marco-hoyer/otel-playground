FROM python:3.9

COPY src /app
COPY requirements.txt /requirements.txt

RUN pip3 install -r /requirements.txt

EXPOSE 6666

CMD ["python", "/app/main.py"]
