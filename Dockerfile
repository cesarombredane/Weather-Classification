# pull a python base image
FROM python:3.10.8

# set the working directory to /app
WORKDIR /app

# copy the requirements file to the working directory
COPY ./requirements.txt .

# install the requirements
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt
RUN python3 -m pip install python-multipart

# copy the python script to the working directory
COPY Weather_Classification_TP.py .
COPY api.py .

# run the python script
CMD ["python3", "Weather_Classification_TP.py", "-y"]
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]