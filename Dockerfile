# pull a python base image (alpine distro is a lightweight version of linux)
FROM python:3.10.12-alpine

RUN apk add --no-cache gcc musl-dev linux-headers
# set the working directory to /app
WORKDIR /app

# copy the requirements file to the working directory
COPY ./requirements.txt .

# install system dependencies
RUN apk update && \
    apk add --no-cache build-base libffi-dev openssl-dev

# install the requirements
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt

# copy the python script to the working directory
COPY Weather_Classification_TP.py .

# run the python script
CMD ["python3", "Weather_Classification_TP.py"]
