# testweb
python-django sample project

1.
docker run -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=djangodocker_db mysql

mysql -h localhost -P 3306 --protocol=tcp -u root -p

CREATE USER 'django'@'%'  IDENTIFIED BY 'django';

ALTER USER 'django'@'%' IDENTIFIED WITH mysql_native_password BY 'django';

DROP DATABASE IF EXISTS django;

CREATE DATABASE django
    DEFAULT CHARACTER SET utf8
    DEFAULT COLLATE utf8_general_ci;

GRANT ALL PRIVILEGES ON django.* TO 'django'@'%' ;

2.

get code from  https://github.com/sreenathd/testweb



docker run -it --entrypoint bash  -p 80:80 --name djangotestweb  -v  localpath:/var/www/testweb sreenathd/testweb 

update settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': 'django',
        'HOST': 'db_container_ip',
        'PORT': '3306'
    }
}

/var/www/testweb# python3 manage.py runserver 0.0.0.0:80
