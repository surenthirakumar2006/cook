FROM alpine:latest
RUN apk add --no-cache python3 py3-flask 
WORKDIR /app
COPY app.py .
EXPOSE 5225
CMD ["python", "app.py"]
