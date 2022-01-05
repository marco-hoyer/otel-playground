FROM python:3.9

COPY src /app
COPY requirements.txt /requirements.txt

RUN pip3 install -r /requirements.txt

EXPOSE 7777

CMD ["python", "/app/main.py"]
