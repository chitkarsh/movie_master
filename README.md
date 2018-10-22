# movie master


### Getting Started
------------------
easy_install mysql-python
pip install -r requirements.txt
create database movies_master;
python -m movies.manage db upgrade
python -m movies.manage seed
