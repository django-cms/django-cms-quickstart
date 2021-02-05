# django CMS quickstart

A Dockerised django CMS project, ready to deploy on [Divio](https://www.divio.com/) or another Docker-based cloud platform, and run locally in Docker on your own machine.

This version uses Python 3.8 running and the most up-to-date versions of Django 3.1 and django CMS 3.8.

## Installation

You need to have docker installed on your system to run this project.

- [Install Docker] (https://docs.docker.com/engine/install/) here.
- If you have not used docker in the past, please read this [introduction on docker](https://docs.docker.com/get-started/) here.

## Try it

```bash
git clone git@github.com:django-cms/django-cms-quickstart.git
cd django-cms-quickstart
docker-compose build
docker-compose run web python manage.py migrate
docker-compose run web python manage.py createsuperuser
docker-compose up
open http://127.0.0.1:8000
```

For a more complete how-to guide to this project, see [Deploy a new django CMS project using the Divio quickstart
repository](https://docs.divio.com/en/latest/how-to/django-cms-deploy-quickstart/) in the [Divio Developer
Handbook](https://docs.divio.com).


## Customising the project

This project is ready-to-go without making any changes at all, but also gives you some options.

As-is, it will include a number of useful django CMS plugins and Bootstrap 4 for the frontend. You don't have to use
these; they're optional. If you don't want to use them, read through the `settings.py` and `requirements.txt` files to
see sections that can be removed - in each case, the section is noted with a comment containing the word 'optional'.

Options are also available for using Postgres/MySQL, uWSGI/Gunicorn/Guvicorn, etc.

## Contribution

This code for this project has been forked from Divio's quickstart repo. We are grateful for their valueable contribution to the code and documentation of this code.

You can follow the original repo [here](https://github.com/divio/django-cms-divio-quickstart/).
