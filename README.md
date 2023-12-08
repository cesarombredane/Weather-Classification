# Software requirements
Need to have Docker & Docker Composed installed on your computer, here is the link that explains what is Docker and how to install it: https://docs.docker.com/desktop/. After installing it, check if you have Docker and Docker Compose by typing respectively in your terminal/command line : 
- `docker --version`
- `docker-compose --version`

If you don't have Docker Compose after the installation of docker (usually it is in it), you can install it by following the instructions here: https://docs.docker.com/compose/install/

# test local (linux environment)

- `python3 -m venv env`  

- `source env/bin/activate`

⚠️ Need to have Python 3.10.8 locally, so to check it :

- `python -- version`

  -> If the output of the previous command is not Python 3.10.8, it needs to be installed using the following command:

  - `pip install --upgrade python==3.10.8`

    After checking, the Python version has to be 3.10.8

-> Otherwise, if the output of `python -- version` is already 3.10.8, you can continue with the following commands :

- `python3 -m pip install -r requirements.txt`

- `python3 Weather_Classification_TP.py`

# run docker

- `docker compose up`
