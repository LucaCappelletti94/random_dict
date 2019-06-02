random_dict
=========================================================================================
|travis| |sonar_quality| |sonar_maintainability| |codacy| |code_climate_maintainability| |pip| |downloads|

Simple python package to generate random dictionaries of given types.

How do I install this package?
----------------------------------------------
As usual, just download it using pip:

.. code:: shell

    pip install random_dict

Tests Coverage
----------------------------------------------
Since some software handling coverages sometime get slightly different results, here's three of them:

|coveralls| |sonar_coverage| |code_climate_coverage|

Usage examples
----------------------------------------------

random_string_dict
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This function will generate a dictionary with given at most `max_depth` and `max_height` of type `string`.

.. code:: python

    from random_dict import random_string_dict
    from random import randint

    random_string_dict(randint(1, 10), randint(1, 10))

random_bool_dict
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This function will generate a dictionary with given at most `max_depth` and `max_height` of type `bool`.

.. code:: python

    from random_dict import random_bool_dict
    from random import randint

    random_bool_dict(randint(1, 10), randint(1, 10))

random_float_dict
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This function will generate a dictionary with given at most `max_depth` and `max_height` of type `float`.

.. code:: python

    from random_dict import random_float_dict
    from random import randint

    random_float_dict(randint(1, 10), randint(1, 10))

random_int_dict
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This function will generate a dictionary with given at most `max_depth` and `max_height` of type `int`.

.. code:: python

    from random_dict import random_int_dict
    from random import randint

    random_int_dict(randint(1, 10), randint(1, 10))

random_dict
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This function will generate a dictionary with given at most `max_depth` and `max_height` of mixed types.

.. code:: python

    from random_dict import random_dict
    from random import randint

    random_dict(randint(1, 10), randint(1, 10))

Some generated examples can be found within the examples folder.

.. |travis| image:: https://travis-ci.org/LucaCappelletti94/random_dict.png
   :target: https://travis-ci.org/LucaCappelletti94/random_dict
   :alt: Travis CI build

.. |sonar_quality| image:: https://sonarcloud.io/api/project_badges/measure?project=LucaCappelletti94_random_dict&metric=alert_status
    :target: https://sonarcloud.io/dashboard/index/LucaCappelletti94_random_dict
    :alt: SonarCloud Quality

.. |sonar_maintainability| image:: https://sonarcloud.io/api/project_badges/measure?project=LucaCappelletti94_random_dict&metric=sqale_rating
    :target: https://sonarcloud.io/dashboard/index/LucaCappelletti94_random_dict
    :alt: SonarCloud Maintainability

.. |sonar_coverage| image:: https://sonarcloud.io/api/project_badges/measure?project=LucaCappelletti94_random_dict&metric=coverage
    :target: https://sonarcloud.io/dashboard/index/LucaCappelletti94_random_dict
    :alt: SonarCloud Coverage

.. |coveralls| image:: https://coveralls.io/repos/github/LucaCappelletti94/random_dict/badge.svg?branch=master
    :target: https://coveralls.io/github/LucaCappelletti94/random_dict?branch=master
    :alt: Coveralls Coverage

.. |pip| image:: https://badge.fury.io/py/random_dict.svg
    :target: https://badge.fury.io/py/random_dict
    :alt: Pypi project

.. |downloads| image:: https://pepy.tech/badge/random_dict
    :target: https://pepy.tech/badge/random_dict
    :alt: Pypi total project downloads 

.. |codacy|  image:: https://api.codacy.com/project/badge/Grade/51be6aeee29e411994d34b6fc6063886
    :target: https://www.codacy.com/app/LucaCappelletti94/random_dict?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=LucaCappelletti94/random_dict&amp;utm_campaign=Badge_Grade
    :alt: Codacy Maintainability

.. |code_climate_maintainability| image:: https://api.codeclimate.com/v1/badges/a04ccb96d15d8f47d3ec/maintainability
    :target: https://codeclimate.com/github/LucaCappelletti94/random_dict/maintainability
    :alt: Maintainability

.. |code_climate_coverage| image:: https://api.codeclimate.com/v1/badges/a04ccb96d15d8f47d3ec/test_coverage
    :target: https://codeclimate.com/github/LucaCappelletti94/random_dict/test_coverage
    :alt: Code Climate Coverate