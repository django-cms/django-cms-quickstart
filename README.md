![Python application](https://github.com/django-cms/django-cms-quickstart/workflows/Python%20application/badge.svg?branch=main)

# django CMS quickstart

A Dockerised django CMS project, ready to deploy on [Divio](https://www.divio.com/) or another Docker-based cloud platform, and run locally in Docker on your own machine.

This version uses Python 3.8 running and the most up-to-date versions of Django 3.1 and django CMS 3.8.

## Installation

You need to have docker installed on your system to run this project.

- [Install Docker](https://docs.docker.com/engine/install/) here.
- If you have not used docker in the past, please read this [introduction on docker](https://docs.docker.com/get-started/) here.

## Try it

```bash
git clone git@github.com:django-cms/django-cms-quickstart.git
cd django-cms-quickstart
docker compose up --force-recreate --build -d
docker compose run web python manage.py migrate
docker compose run web python manage.py createsuperuser
```

Then open http://django-cms-quickstart.127.0.0.1.nip.io:8000 (or just http://127.0.0.1:8000) in your browser.

## Customising the project

This project is ready-to-go without making any changes at all, but also gives you some options.

As-is, it will include a number of useful django CMS plugins and Bootstrap 4 for the frontend. You don't have to use
these; they're optional. If you don't want to use them, read through the `settings.py` and `requirements.txt` files to
see sections that can be removed - in each case, the section is noted with a comment containing the word 'optional'.

Options are also available for using Postgres/MySQL, uWSGI/Gunicorn/Guvicorn, etc.

## Features

### Static Files with Whitenoise

This quickstart demo has a cloud-ready static files setup via django-whitenoise.

In the containerized cloud the application is not served by a web server like nginx but directly through uwsgi. django-whitenoise is the glue that's needed to serve static files in your application directly through uwsgi.

See the django-whitenoise settings in settings.py and the `quickstart/templates/whitenoise-static-files-demo.html` demo page template that serves a static file.

## Contribution

Here is the official django CMS repository: [https://github.com/django-cms/django-cms-quickstart/](https://github.com/django-cms/django-cms-quickstart/).


## Deployment

Note that this is just a demo project to get you started. If you want a full production ready site with all the bells and whistles we recommend you have a look at https://github.com/django-cms/djangocms-template instead.

#### Env variables
- to deploy this project in testing mode (recommended) set the environment variable `DEBUG` to `True` in your hosting environment. 
- For production environment (if `DEBUG` is false) django requires you to whitelist the domain. Set the env var `DOMAIN` to the host, i.e. `www.domain.com` or `*.domain.com`.
- If you want the media hosted on S3 set the `DEFAULT_FILE_STORAGE` variable accordingly.

#### Deployment Commands
Configure your hosting environment to run the following commands on every deployment:
- `./manage.py migrate`


#### Divio Deployment

divio.com is a cloud hosting platform optimized for django web applications. It's the quickest way to deploy this project. Here is a [video tutorial](https://www.youtube.com/watch?v=O2g5Wfoyp7Q) and a [description of the deployment steps](https://github.com/django-cms/djangocms-template/blob/mco-standalone/docs/deployment-divio.md#divio-project-setup) that are mostly applicable for this quickstart project.
