# django-affiliate-marketing
Django Affiliate Marketing Website

## Running Locally

```sh
$ git clone https://github.com/goldminer1030/django-affiliate-marketing.git
$ cd django-affiliate-marketing

$ python3 -m venv django-affiliate-marketing
$ pip install -r requirements.txt

$ createdb django-affiliate-marketing

$ python manage.py migrate
$ python manage.py collectstatic

$ heroku local
```

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master

$ heroku run python manage.py migrate
$ heroku open
```