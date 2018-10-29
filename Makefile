# lists all available targets
list:
	@sh -c "$(MAKE) -p no_targets__ | awk -F':' '/^[a-zA-Z0-9][^\$$#\/\\t=]*:([^=]|$$)/ {split(\$$1,A,/ /);for(i in A)print A[i]}' | grep -v '__\$$' | grep -v 'make\[1\]' | grep -v 'Makefile' | sort"
# required for list
no_targets__:

export FLASK_CONFIG=dev
setup:	setup-pyc, setup-build, setup-python

setup-clean:
	@find . -name '*py[c~]' -delete

setup-build:
	rm --force --recursive build/
	rm --force --recursive dist/
	rm --force --recursive *.egg-info

setup-python:
	@pip install -e .
	
setup-logging:
	@mkdir /var/log/movies
	@chmod 777 /var/log/movies

setup-db:
	setup-migrate
	 	
setup-migrate:
	@python -m movies.manage db upgrade
	@python -m movies.manage seed
	
run-flask:
	@export export FLASK_ENV=development
	@export export FLASK_APP=movies
	@export export FLASK_RUN_PORT=5002
	@python -m flask run	

# mysql-config is required for mySQLdb, a python interface for MySQL so,
#sudo apt-get install libmysqlclient-dev