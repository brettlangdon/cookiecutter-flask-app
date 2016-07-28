cookiecutter-flask-app
======================

My own personal `cookiecutter <https://cookiecutter.readthedocs.io/en/latest/>`_ template for writing `Flask <https://http://flask.pocoo.org/>`_ apps.

This cookiecutter sets up a starter Flask app using:

* `Flask <https://http://flask.pocoo.org/>`_
* `Flask-Assets <https://flask-assets.readthedocs.io>`_
* `Flask-Migrate <http://flask-migrate.readthedocs.io/>`_
* `Flask-Script <http://flask-script.readthedocs.io/>`_
* `Flask-Security <http://flask-security.readthedocs.io/>`_
* `Flask-SQLAlchemy <http://flask-sqlalchemy.readthedocs.io/>`_
* `libsass-python <https://hongminhee.org/libsass-python/>`_
* `webassets-browserify <https://github.com/renstrom/webassets-browserify>`_


Usage
-----

To create a new starting project:

.. code-block:: bash

    # Create new project folder from the skeleton
    pip install cookiecutter
    cookiecutter https://github.com/brettlangdon/cookiecutter-flask-app.git
    cd ./project_name

    # Setup new virtualenv and install dependencies
    mkvirtualenv project_name
    pip install -r requirements.txt
    npm install

    # Start the server
    python -m project_name runserver

    # Or, start using project script
    PYTHONPATH. ./bin/project_name runserver
