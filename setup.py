"""Millipede installation script

https://github.com/getmillipede/millipede-python
"""

from setuptools import setup, find_packages
from codecs import open as copen
import os


MODULE_NAME = 'millipede'


def get_long_description():
    """ Retrieve the long description from DESCRIPTION.rst """
    here = os.path.abspath(os.path.dirname(__file__))

    with copen(os.path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as description:
        return description.read()

def get_version():
    """ Retrieve version information from the package """
    return __import__('millipede').__version__


setup(
    name=MODULE_NAME,
    version=get_version(),
    description="THE millipede generator",
    long_description=get_long_description(),

    url="https://github.com/getmillipede/millipede-python",

    author="Millipede Team",
    author_email="hello@millipede.io",

    license="MIT",

    extras_require={
        'sms': ['requests']
    },

    classifiers=[
        'Development Status :: 5 - Production/Stable',

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

    test_suite="tests",

    keywords="millipede",

    entry_points={
        'console_scripts': [
            'millipede=millipede:main',
        ],
    },
)
