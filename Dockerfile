FROM python:3.10
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .
EXPOSE 8080
CMD ["hypercorn", "--bind", "0.0.0.0:8080", "app:app"]