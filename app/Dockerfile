FROM python:3.11-alpine
WORKDIR /opt/app

ENV DB_USER=postgres
ENV DB_PASSWORD=postgres
ENV DB_HOST=sql
ENV DB_PORT=5432
ENV DB_NAME=bewise2

RUN apk add --no-cache gcc musl-dev linux-headers ffmpeg
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8080

CMD ["python", "-m", "uvicorn", "main:app", "--port", "8080", "--host", "0.0.0.0"]