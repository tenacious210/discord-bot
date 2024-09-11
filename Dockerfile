FROM python:3.11-alpine

WORKDIR /discord-bot
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN adduser -D appuser
RUN mkdir -p /discord-bot/config && chown -R appuser:appuser /discord-bot/config
USER appuser

ENTRYPOINT ["python", "main.py"]