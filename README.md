# django CMS Divio quickstart

A Dockerised django CMS project, ready to deploy on Divio or another Docker-based cloud platform, and run
locally in Docker on your own machine. A Divio account is not required.

This version uses Python 3.8 running and the most up-to-date versions of Django 3.1 and django CMS 3.8.

For a complete how-to guide for this project, see [Deploy a new django CMS project using the Divio quickstart
repository](https://docs.divio.com/en/latest/how-to/django-cms-deploy-quickstart/) in the [Divio Developer
Handbook](https://docs.divio.com).

The guide shows you how to use this repository to deploy a Twelve-factor Django project including Postgres or MySQL,
and cloud media storage using S3, with Docker. It also gives you a fully working local project for development,
also running in Docker.

## Important

This project is ready-to-go, but also gives you some options. As-is, it will include a number of useful django CMS
plugins and Bootstrap 4 for the frontend. You don't have to use these; they're optional. If you don't want to use them,
read through the `settings.py` and `requirements.txt` files to see sections that can be removed - in each case, the
section is noted with a comment containing the word 'optional'.
