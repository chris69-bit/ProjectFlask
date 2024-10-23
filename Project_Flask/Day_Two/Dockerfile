#Use the official python runtime as the base image 
FROM python:3.9-slim

#Create a working directory inside the container
WORKDIR /app

#Install SQLite dependencies
RUN apt-get update -qq $$ apt-get install sqlite3 libsqlite3-dev

#Copy and install dependencies
COPY requirements.txt /app
RUN pip install -r requirements.txt

#Copy the rest of the application
COPY . /app/

#Expose port
EXPOSE 3000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "wsgi:app"]