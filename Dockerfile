FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /app
EXPOSE 5000
CMD ["python3", "app.py", "--host=0.0.0.0"]
