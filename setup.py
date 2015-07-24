"""Millipede installation script

https://github.com/evadot/millipede
"""

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="millipede",
    version="0.1",
    description="A millipede generator",
    long_description=long_description,

    url="https://github.com/evadot/millipede"

    author="The millipede fan club"

    license="MIT"

    classifiers=[
        'Development Status :: 4 - Alpha',

        'Intended Audience :: Religion',
        'Topic :: Religion'
        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    keywords="millipede",

    entry_points={
        'console_scripts': [
            'millipede=millipede:main',
        ],
    },
)
