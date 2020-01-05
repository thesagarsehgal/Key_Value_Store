# using the latest version of a basic light weight alpine os 
FROM alpine:latest

# install python3-dev
RUN apk add --no-cache python3-dev 
# upgrade python3 pip
RUN pip3 install --upgrade pip
# copy requirements.txt to /tmp/
COPY ./requirements.txt /tmp/
# install the dependencies in the requirements.txt recursively
RUN pip3 install -r /tmp/requirements.txt

# making a repo where the code would be copied
RUN mkdir /app
# copying the code present in ./app to /app of the container
COPY ./app /app
# shift the working directory to /app
WORKDIR /app

# expose the port on which the app would be working
EXPOSE 5000

ENTRYPOINT ["gunicorn"]
# gunicorn --workers=4 --bind 0.0.0.0:5000 wsgi:app
CMD ["--workers","4","--bind", "0.0.0.0:5000", "wsgi:app"]
