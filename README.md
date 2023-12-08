# Software requirement
Need to have Docker & Docker Composed installed on your computer, here is the link that explains what is Docker and how to install it: https://docs.docker.com/desktop/. After installing it, check if you have Docker and Docker Compose by typing respectively in your terminal/command line : 
- `docker --version`
- `docker-compose --version`

If you don't have Docker Compose after the installation of docker (usually it is in it), you can install it by following the instructions here: https://docs.docker.com/compose/install/

# test local (linux environment)

- `python3 -m venv env`

- `source env/bin/activate`

- `python3 -m pip install -r requirements.txt`

- `python3 Weather_Classification_TP.py`

# run docker

- `docker compose up`
