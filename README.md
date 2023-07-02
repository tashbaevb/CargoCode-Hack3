# Real socket django chat api
### Before running

**You must install Redis Database**

To install and use redis on windows [check here](https://redis.com/blog/redis-on-windows-10/).
To install and use redis on Linux [check here](https://linuxtechlab.com/how-install-redis-server-linux/). 



### How to run this 


``` bash
poetry install

python manage.py createsuperuser

python manage.py makemigrations
python manage.py migrate

python manage.py runserver
```

### The API docs

You can check the API docs [here](https://documenter.getpostman.com/view/15225360/TzzEouP9)
