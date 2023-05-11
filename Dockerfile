# base image  
FROM python:3.10-slim-bullseye
RUN apt update
RUN apt install -y cups
RUN apt install -y default-jre libreoffice-core libreoffice-common libreoffice-java-common
RUN apt install -y --no-install-recommends libreoffice-writer libreoffice-gtk3
# RUN usermod -aG lpadmin pi
# setup environment variable  
COPY . /app  
# where your code lives  
WORKDIR /app/

# set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

# install dependencies  
RUN pip install --upgrade pip  

# copy whole project to your docker home directory. 
# run this command to install all dependencies  
RUN pip install -r requirements.txt  
# port where the Django app runs  
EXPOSE 8000  
# start server  
RUN python manage.py shell < initial_setup.py
CMD python manage.py runserver 0.0.0.0:8000
