#Use the official runtime as the base image
FROM python:3.9-slim

#Create a working directory inside the container
WORKDIR /app

#Install sqlite dependencies
RUN apt-get update -qq && apt-get install -y sqlite3 build-essential libsqlite3-dev 

#Copy and install dependencies
COPY requirements.txt /app
RUN pip install -r requirements.txt

#Copy the rest of the application
COPY . .

#Expose the rest of the application
EXPOSE 5000

#Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "wsgi:app"]