FROM ubuntu:20.04
RUN apt-get update -y
COPY . /app
WORKDIR /app
RUN set -xe \
    && apt-get update -y \
    && apt-get install -y python3-pip \
    && apt-get install -y mysql-client 
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 81
ENTRYPOINT ["sh", "-c", "ls /app -lR && python3 getbg.py && sleep 2 && python3 app.py"]
# CMD [ "app.py" ]