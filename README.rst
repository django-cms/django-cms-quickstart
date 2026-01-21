############################
🚀 django CMS Quickstart
############################

**Get a modern django CMS site running locally in minutes — powered by Docker.**

This repository provides an **official, dockerised django CMS starter project** designed for:

- Local development 💻
- Docker-based cloud platforms ☁️ (e.g. Divio)
- Fast experimentation and learning 🧪

----

✨ What’s Inside?
#################

- 🐍 **Python 3.13**, 🎯 **Django 5.2**, 🧩 **django CMS 5.0**
- 🐳 Fully **Docker Compose** based
- 🏗️ Cloud-ready configuration
- 🎨 djangocms-frontend Bootstrap 5 components (optional)
- 🔌 Curated set of useful django CMS plugins

**Officially endorsed by the django CMS Association**
This project aligns with the official django CMS roadmap and plugin policy.

📚 Documentation: https://docs.django-cms.org/
💬 Community & Support: https://www.django-cms.org/slack/

----

🧑‍💻 Quick Start (5 Minutes)
##########################

Prerequisites
=============

You only need **Docker** installed.

- Install Docker: https://docs.docker.com/engine/install/
- New to Docker? Start here: https://docs.docker.com/get-started/

----

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

Open your browser:

- http://django-cms-quickstart.127.0.0.1.nip.io:8000
- or http://127.0.0.1:8000

----

Managing the Project
====================

- Stop containers (keep data):

  ``docker compose stop``

- Restart:

  ``docker compose start``

- Remove containers (keep database & media):

  ``docker compose down``

Data persistence:

- PostgreSQL: ``django-cms-quickstart_postgres-data``
- Media files: ``data/media``

----

⚙️ Customisation Options
########################

This project works **out of the box**, but is also easy to tailor.

Optional customisations include:

- Removing Bootstrap 5
- Removing bundled plugins
- Switching databases (PostgreSQL / MySQL)
- Switching servers (uWSGI / Gunicorn / Guvicorn)

Look for sections marked **optional** in:

- ``settings.py``
- ``requirements.txt``

----

🧪 Load Demo Content (Recommended)
##################################

Quickly explore django CMS with some pre-built pages.

1. List available demo pages:

   ``docker compose run --rm web python manage.py democontent``

2. Load a page:

   ``docker compose run --rm web python manage.py democontent <FILE_PATH>``

3. Force overwrite:

   ``docker compose run --rm web python manage.py democontent <FILE_PATH> --force``

----

📦 Dependency Management
########################

This project uses **pip-tools** for clean and reproducible dependency locking.

Updating Requirements
=====================

1. Edit ``requirements.in``
2. Compile dependencies:

   .. code-block:: bash

     docker compose run --rm web pip-compile requirements.in >> requirements.txt

3. Rebuild containers:

   .. code-block:: bash

     docker compose build web
     docker compose up -d

----

🧠 Key Features
###############

Static Files with Whitenoise
============================

- Cloud-ready static file handling
- No external web server required
- Served directly via uWSGI

Example template:

- ``quickstart/templates/whitenoise-static-files-demo.html``

----

Environment Variables
=====================

- ``.env-local`` is injected automatically
- Expose PostgreSQL to host by setting ``DB_PORT``
- If unset, PostgreSQL is only reachable within Docker

----

🤝 Contributing
###############

Contributions, feedback, and improvements are welcome.

----

🚢 Deployment Notes
###################

This project is intended as a **starter/demo**.

For a production-ready setup, see:

https://github.com/django-cms/djangocms-template

Production Tips
===============

- Set ``DEBUG=True`` for testing environments
- Set ``DOMAIN`` when ``DEBUG=False``
- Configure ``DEFAULT_STORAGE_DSN`` for S3 or similar storage

Required Deployment Command
===========================

``./manage.py migrate``

----

☁️ Divio Deployment
###################

Divio is optimized for Django and django CMS.

Video tutorial:
https://www.youtube.com/watch?v=O2g5Wfoyp7Q

Deployment guide:
https://github.com/django-cms/djangocms-template/blob/mco-standalone/docs/deployment-divio.md#divio-project-setup

----

Happy building!
If this helped you, ⭐️ the repository and join the django CMS community.
