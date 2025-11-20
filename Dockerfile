FROM python:3.12-slim
WORKDIR /app
COPY . /app
RUN pip install fastapi uvicorn pydantic
EXPOSE 8005
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8005"]
