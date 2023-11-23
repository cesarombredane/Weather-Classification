FROM python:3.8

WORKDIR /app

COPY ./requirements.txt .
RUN python3 -m pip install -r requirements.txt
COPY Weather_Classification_TP.py .

CMD ["python3", "Weather_Classification_TP.py"]
