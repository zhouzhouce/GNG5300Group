# GNG5300Group
For GNG5300 course group projects

## MySQL
### Install mysql with a proper version
https://dev.mysql.com/downloads/mysql/

### Configure environment variable (for macOS, if /usr/local/mysql/bin/ is not in your PATH enviroment variable)
```
export PATH=${PATH}:/usr/local/mysql/bin/
```

### Create new db in mysql with the same name in settings.py
```
CREATE DATABASE fitness_testdb;
```

### Create a user in mysql with the same name in settings.py
```
CREATE USER 'test'@'localhost' IDENTIFIED BY 'secret_1234';
```

### Grant all privileges to the newly created user
```
GRANT ALL PRIVILEGES ON `fitness_testdb` . * TO 'test'@'localhost';
FLUSH PRIVILEGES; 
```

### Install python driver for mysql
```
pip install mysql client
```

### Install related python library (if needed)
```
pip install PyMySQL
pip install cryptography
pip install django-mysql
```

## Cerely
### Install redis
https://redis.io/docs/getting-started/

### Install required packages
```
pip install celery
pip install django-celery-results
pip install django-celery-beat
```

### Migrate for first use to create all the models related to celery and celery-beat
```
python manage.py migrate
```

### Run redis
```
redis-server
```

### Start celery in new terminal
```
celery -A fitness_management_system worker --pool=solo -l info
```

### Start celery beat in new terminal
```
celery -A fitness_management_system beat -l INFO
```

### Run the below command if you want to kill the workers
```
celery -A fitness_management_system purge
```


## Test
### Grant the privileges on test db before creating any test case in test.py
```
GRANT ALL PRIVILEGES ON test_fitness_testdb.* TO 'test'@'localhost';
```

## Load initial data
```
python manage.py loaddata login/fixtures/initial_data.json
```