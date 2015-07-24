"""Millipede installation script

https://github.com/evadot/millipede
"""

from setuptools import setup, find_packages
from codecs import open
import os
import re


MODULE_NAME = 'millipede'


here = os.path.abspath(os.path.dirname(__file__))


with open(os.path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()


def get_version():
    """ Reads package version number from package's __init__.py. """
    with open(os.path.join(
        os.path.dirname(__file__), MODULE_NAME, '__init__.py'
    )) as init:
        for line in init.readlines():
            res = re.match(r'^__version__ = [\'"](.*)[\'"]$', line)
            if res:
                return res.group(1)
    raise ValueError('No __version__ found in __init__.py')


setup(
    name=MODULE_NAME,
    version=get_version(),
    description="THE millipede generator",
    long_description=long_description,

    url="https://github.com/evadot/millipede",

    author="The millipede fan club",
    author_email="millipede@bidouilliste.com",

    license="MIT",

    extras_require={
        'sms': ['requests']
    },

    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Religion',
        'Topic :: Religion',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),

    keywords="millipede",

    entry_points={
        'console_scripts': [
            'millipede=millipede:main',
        ],
    },
)
