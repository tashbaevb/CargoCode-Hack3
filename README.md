# Cargo Code Hack Site
### Before running

**You must install Redis Database to store chat data**

To install and use redis on windows [check here](https://redis.com/blog/redis-on-windows-10/).
To install and use redis on Linux [check here](https://linuxtechlab.com/how-install-redis-server-linux/). 

### Байтемир

**Нужно срочно протестировать бэк чата из фронта, так как я не уверен в некоторых вещах**

### How to run this 


``` bash
poetry install

python manage.py createsuperuser

python manage.py makemigrations
python manage.py migrate

python manage.py runserver
```

### The chat API docs

You can check the chat API docs [here](https://documenter.getpostman.com/view/15225360/TzzEouP9)




