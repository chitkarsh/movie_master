# Python Flask Movie Manager Application

This is an API based application (no UI) which holds movie information. Users can view list of movies and its details. Users also have the functionality to search for movies based on director, genre, score, popularity. Admins can create, delete, update movie listings. Admin Users are authenticated using JWT tokens

[API Documentation](https://github.com/chitkarsh/movie_master/wiki/API-Documentation)

### Pre-requisites
To use this application you must have Python 2.7.9 and above installed (if not please visit [python download page](https://www.python.org/downloads/release/python-2712/)), PIP - Python package manager (if not please check [installation guide](https://pip.pypa.io/en/stable/installing/)) and MySQL installed and running (if not please check out [MySQL download page](https://pip.pypa.io/en/stable/installing/) and follow [instructions](http://dev.mysql.com/doc/refman/5.7/en/installing.html))

To check your installations, run the following command in the command line:
```sh
$ python --version
Python 2.7.15 # sample output
$ pip -V
pip 18.1 from /usr/lib/python2.7/dist-packages (python 2.7) # sample output
$ mysql --version
mysql  Ver 14.14 Distrib 5.5.52, for debian-linux-gnu (x86_64) using readline 6. # sample output
```

### Getting Started

Clone the repository to your local workspalce
```sh
$ git clone https://github.com/chitkarsh/movie_master.git
```
Navigate to the repository folder:
```
$ cd movie_master
```

create virtualenv space and Install dependencies:
```sh
# Installing mysql-python first as it may give errors especially on windows
$ easy_install  MySQL-python
# If above fails, download corresponding wheel from https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysql-python and install it with pip

# install all other dependencies
$ pip install -r requirements.txt
```

Set up MySQL database, use -u -p flags to provide username and password:
```sh
$ mysql -uroot
$ mysql>  CREATE DATABASE movie_master;
```
Setting up config:
- In /instance dir, you will see app_config.py.sample
- Edit the config parameters. (Reccomend to only edit the db connection string)
- Save the file as app_config.py in /instance dir

Migrate and seed the database:
```sh
# set/export the FLASK_CONFIG to dev, stage, prod
# windows   : set FLASK_CONFIG=dev
# linux     : export FLASK_CONFIG=dev

$ python -m movies.manage db upgrade
$ python -m movies.manage seed

# if you face trouble in alembic version, delete the /migration dir and run the following commands
$ python -m movies.manage db init
$ python -m movies.manage db migrate
$ python -m movies.manage db upgrade
$ python -m movies.manage seed
```

Run the Application:

On Linux-
```sh
$ FLASK_CONFIG=dev FLASK_ENV=development FLASK_APP=movies FLASK_RUN_PORT=5002 python -m flask run
```

On Windows-
```sh
set FLASK_CONFIG=dev
set FLASK_ENV=development
set FLASK_APP=movies
set FLASK_RUN_PORT=5002
python -m flask run
```
Open browser at http://127.0.0.1:5002/

[API Documentation](https://github.com/chitkarsh/movie_master/wiki/API-Documentation)
