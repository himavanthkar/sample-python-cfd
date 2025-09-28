# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "food-delivery-api"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion>=2.0.2", "swagger-ui-bundle>=0.0.2", "python_dateutil>=2.6.0"]

setup(
    name=NAME,
    version=VERSION,
    description="Continuous Food Delivery API - Restaurant Management Backend",
    author_email="",
    url="",
    keywords=["OpenAPI", "Food Delivery", "Restaurant API", "Flask", "REST API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={"": ["openapi/openapi.yaml"]},
    include_package_data=True,
    entry_points={"console_scripts": ["food-delivery-api=openapi_server.__main__:main"]},
    long_description="""\
    A complete food delivery backend API built with Flask and Connexion. 
    Provides restaurant menu management, shopping cart functionality, and image upload capabilities.
    Features a full OpenAPI/Swagger specification for easy integration with frontend applications.
    """,
)