# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "swagger_server"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion"]

setup(
    name=NAME,
    version=VERSION,
    description="Argument Store",
    author_email="m.schmid@ajato.ch",
    url="",
    keywords=["Swagger", "Argument Store"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['swagger_server=swagger_server.__main__:main']},
    long_description="""\
    The Argument Store application targets to improve political discussions. This is achieved via clustered argument collection, as well as user rated arguments. The arguments are sorted into topics. The app is going to be distributed via Cloud and will be available as a SPA webapp.
    """
)
