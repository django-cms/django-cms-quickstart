|pythonapp|

#####################
django CMS quickstart
#####################

- A dockerised django CMS project intended to be run locally in Docker on your own machine or on a Docker-based cloud, such as `Divio <https://www.divio.com/>`_ 
- This version uses Python 3.11 and the most up-to-date versions of Django 4.2, and django CMS 4.1.0
- This project is endorsed by the `django CMS Association <https://www.django-cms.org/en/about-us/>`_. That means that it is officially accepted by the dCA as being in line with our roadmap vision and development/plugin policy. Join us on `Slack <https://www.django-cms.org/slack/>`_ for more information or questions.
- The documentation for  django CMS can be found here: https://docs.django-cms.org/

Installation
############

Requirements
============

You need to have Docker installed on your system to run this project.

- `Install Docker <https://docs.docker.com/engine/install/>`_ here.
- If you have not used docker in the past, please read this
  `introduction on docker <https://docs.docker.com/get-started/>`_  here.

Local Setup
===========

.. inclusion-marker-do-not-remove

.. code-block:: bash

  git clone git@github.com:django-cms/django-cms-quickstart.git
  cd django-cms-quickstart
  docker compose build web
  docker compose up -d database_default
  docker compose run --rm web python manage.py migrate
  docker compose run --rm web python manage.py createsuperuser
  docker compose up -d

Then open http://django-cms-quickstart.127.0.0.1.nip.io:8000 (or just http://127.0.0.1:8000) in your browser.

You can stop the server with ``docker compose stop`` without destroying the containers and restart it with
``docker compose start``.

With ``docker compose down`` the containers are deleted, but the database content is still preserved in the named
volume ``django-cms-quickstart_postgres-data`` and the media files are stored in the file system in ``data/media``.
Then you can update the project e. g. by changing the requirements and settings. Finally you can rebuild the web image
and start the server again:

.. code-block:: bash

  docker compose build web
  docker compose up -d


Note: Since Compose V2, ``docker-compose`` is now included inside docker. For more information, checkout the
`Compose V2 <https://docs.docker.com/compose/cli-command/>`_ Documentation.

.. inclusion-end-marker-do-not-remove

Customising the project
#######################

This project is ready-to-go without making any changes at all, but also gives you some options.

As-is, it will include a number of useful django CMS plugins and Bootstrap 4 for the frontend. You don't have to use
these; they're optional. If you don't want to use them, read through the ``settings.py`` and ``requirements.txt`` files
to see sections that can be removed - in each case, the section is noted with a comment containing the word 'optional'.

Options are also available for using Postgres/MySQL, uWSGI/Gunicorn/Guvicorn, etc.

Loading with pre-built page on install
======================================

It is now possible to load the project with contents which shows how to use
``django-cms`` and ``djangocms-frontend`` to add pages.

Here is how to use the command:
1. To list the available files in the ``democontent`` folder.
   Run ``docker compose run --rm web python manage.py democontent``

2. To add a page. Run ``docker compose run --rm web python manage.py democontent <FILE_PATH>``

3. To add a page by force. Run ``docker compose run --rm web python manage.py democontent <FILE_PATH> --force``

Updating requirements
=====================

The project uses a django best practise two step approach, freezing all dependencies with pip-tools. Here is how to update requirements:

1. Change ``requirements.in`` according to your needs. There is no need to pin the package versions here unless you have a good reason (i.e. known incompatibilities)
2. Run ``docker compose run --rm web pip-compile requirements.in >> requirements.txt``
3. ``requirements.txt`` should now have changed
4. Rebuild the container ``docker compose build web`` and restart ``docker compose up -d``

Features
########

Static Files with Whitenoise
============================

- This quickstart demo has a cloud-ready static files setup via django-whitenoise.
- In the containerized cloud the application is not served by a web server like nginx but directly through uwsgi. django-whitenoise is the glue that's needed to serve static files in your application directly through uwsgi.
- See the django-whitenoise settings in settings.py and the ``quickstart/templates/whitenoise-static-files-demo.html`` demo page template that serves a static file.

Env variables
=============

- By default, Docker injects the env vars defined in ``.env-local`` into the quickstart project.
- If you want to access the PostgreSQL database from the host system, set ``DB_PORT`` to the desired port number.
  5432 is the standard port number. If you run PosgreSQL on your host system, you may want to set another port number.
  If this variable is empty (the default), the PosgreSQL instance in the container is only reachable within docker, but
  not from outside.

Contribution
############

Here is the official django CMS repository:
`https://github.com/django-cms/django-cms-quickstart/ <https://github.com/django-cms/django-cms-quickstart/>`_.


Deployment
##########

Note that this is just a demo project to get you started. It is designed to be run locally through docker. If you want a full production ready site with all the bells
and whistles we recommend you have a look at https://github.com/django-cms/djangocms-template instead.

Some deployment hints:

- To deploy this project in testing mode (recommended) set the environment variable ``DEBUG`` to ``True`` in your hosting environment.
- Be aware that if ``DEBUG`` is false, django requires you to whitelist the domain. Set the env var ``DOMAIN`` to the host, i.e. ``www.domain.com`` or ``*.domain.com``.
- You can set the env var ``DEFAULT_STORAGE_DSN`` to something meaningful (i.e. for s3 file storage)

Deployment Commands
===================

Configure your hosting environment to run the following commands on every deployment:

- ``./manage.py migrate``


Divio Deployment
================

divio.com is a cloud hosting platform optimized for django web applications. It's the quickest way to deploy this
project. Here is a `video tutorial <https://www.youtube.com/watch?v=O2g5Wfoyp7Q>`_ and a
`description of the deployment steps <https://github.com/django-cms/djangocms-template/blob/mco-standalone/docs/deployment-divio.md#divio-project-setup>`_ that are mostly applicable for this quickstart project.


.. |pythonapp| image:: https://github.com/django-cms/django-cms-quickstart/workflows/Python%20application/badge.svg?branch=support/cms-4.1.x
