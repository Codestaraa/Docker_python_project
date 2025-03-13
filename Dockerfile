FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install flask
RUN pip install requests  # Install the requests package
EXPOSE 5000
CMD ["python", "app.py"]
