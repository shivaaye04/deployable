# base image
FROM python:3.11-slim

# working directory
WORKDIR /app

# copy files
COPY . /app

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# expose port
EXPOSE 8000

# run API
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]