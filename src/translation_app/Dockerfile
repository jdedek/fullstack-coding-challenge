FROM python:3.7.5-stretch

LABEL maintainer "Julien Dedek <jdedek@posteo.de>"

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app 
COPY . /app

# update to get latest packages
RUN apt-get update -y

# Install the dependencies
RUN pip install --upgrade pip -r requirements.txt

# run the command to start uWSGI
#ENTRYPOINT ["uwsgi", "app.ini"]
RUN chmod +x ./start.sh
CMD ["./start.sh"]