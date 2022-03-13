FROM python:latest
WORKDIR /app
COPY test.py ./
CMD [ "python", "./vam_test.py"]

