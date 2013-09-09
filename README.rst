Boulange
========

.. image:: https://travis-ci.org/Ateoto/django-boulange.png?branch=master   
    :target: https://travis-ci.org/Ateoto/django-boulange

.. image:: https://coveralls.io/repos/Ateoto/django-boulange/badge.png?branch=master
    :target: https://coveralls.io/r/Ateoto/django-boulange

Pastry inventory tracker.

Installation
------------

To get the latest stable release from PyPi

.. code-block:: bash

    $ pip install django-boulange

To get the latest commit from GitHub

.. code-block:: bash

    $ pip install -e git+git://github.com/Ateoto/django-boulange.git#egg=boulange

TODO: Describe further installation steps (edit / remove the examples below):

Add ``boulange`` to your ``INSTALLED_APPS``

.. code-block:: python

    INSTALLED_APPS = (
        ...,
        'boulange',
    )

Add the ``boulange`` URLs to your ``urls.py``

.. code-block:: python

    urlpatterns = patterns('',
        ...
        url(r'^pastry/', include('boulange.urls')),
    )

Don't forget to migrate your database

.. code-block:: bash

    ./manage.py migrate boulange


Usage
-----

TODO: Describe usage or point to docs. Also describe available settings and
templatetags.


Contribute
----------

If you want to contribute to this project, please perform the following steps

.. code-block:: bash

    # Fork this repository
    # Clone your fork
    $ mkvirtualenv -p python2.7 django-boulange
    $ python setup.py install
    $ pip install -r dev_requirements.txt

    $ git co -b feature_branch master
    # Implement your feature and tests
    $ git add . && git commit
    $ git push -u origin feature_branch
    # Send us a pull request for your feature branch
