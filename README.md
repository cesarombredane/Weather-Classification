# Software requirements
Need to have **Docker & Docker Composed** installed on your computer, here is the link that explains what is Docker and how to install it: https://docs.docker.com/desktop/. After installing it, check if you have Docker and Docker Compose by typing respectively in your terminal/command line : 
- `docker --version`
- `docker-compose --version`

If you don't have Docker Compose after the installation of docker (usually it is in it), you can install it by following the instructions here: https://docs.docker.com/compose/install/

As the files were large, we used **Git LFS** :
1. You can install it by following this link and the instructions provided there: [https://git-lfs.com/](https://git-lfs.com/).
2. Afterward, clone the repo and navigate to it using `cd`.
3. Next, use the commands `git lfs install` and `git lfs fetch` to fetch the objects in the project. Finally, use the command `git lfs checkout` to download the LFS files."


# test local (linux environment)

1. Need to create a virtual environment for a Python project :
- `python3 -m venv env`  

2. Have to activate the virtual environment created by the previous command using :
- `source env/bin/activate`

⚠️ Need to have Python 3.10.8 locally, so to check it :

- `python -- version`

  -> If the output of the previous command is not Python 3.10.8, it needs to be installed using the following command:

  - `pip install --upgrade python==3.10.8`

    After checking, the Python version has to be 3.10.8

-> Otherwise, if the output of `python -- version` is already 3.10.8, you can continue with the following commands :

3. Have to download all the packages requirements :
- `python3 -m pip install -r requirements.txt`

4. And finally have to run it :
- `python3 Weather_Classification_TP.py`

# run docker

- `docker compose up`
