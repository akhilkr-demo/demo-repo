FROM python:3.8-slim
WORKDIR /app
COPY script.py .
RUN pip install pandas numpy
CMD ["python", "script.py"]
