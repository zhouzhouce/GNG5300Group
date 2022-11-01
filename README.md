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
```
