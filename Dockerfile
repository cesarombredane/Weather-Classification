# pull a python base image (alpine distro is a lightweight version of linux)
FROM python:3.10.12-alpine

# set the working directory to /app
WORKDIR /app

# copy the requirements file to the working directory
COPY ./requirements.txt .

# install the requirements
RUN python3 -m pip install -r requirements.txt

# copy the python script to the working directory
COPY Weather_Classification_TP.py .

# run the python script
CMD ["python3", "Weather_Classification_TP.py"]
