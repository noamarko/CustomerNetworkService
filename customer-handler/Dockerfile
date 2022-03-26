from python:3.9
RUN apt-get update -y && apt-get install -y python3-dev build-essential
COPY . /customer-handler
WORKDIR ./customer-handler
RUN pip install -r ./requirements.txt
CMD ["uvicorn", "app:app", "--host", "0.0.0.0"]