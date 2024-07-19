FROM python:3.12.4-slim-bullseye

EXPOSE 8080

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD [ "fastapi", "run", "main.py", "--port", "8080" ]
