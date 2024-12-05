FROM python:3.11-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

CMD ["python", "-m", "smtpd", "-c", "DebuggingServer", "-n", "localhost:1025"]
