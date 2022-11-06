# GNG5300Group
For GNG5300 course group projects

## Install Python related library
###  Execute following commands:
```
pip install -r requirements.txt
```


## MySQL
### Install mysql with a proper version
https://dev.mysql.com/downloads/mysql/

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
