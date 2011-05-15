README = """==============================
THAT - the Python anti-zen
==============================

Warning: This is a joke. Don't use these bits unless you want to be hated.

Installation
============

At some point this will be packaged up and placed on PyPI. Then you'll be able to just do::

    pip install that

Or if you want to try and play with the awesome source code::

    git clone git@github.com:pydanny/that.git

Usage
======

From the Python shell::

    import that

Enjoy the wisdom!

Contributing
============

Clearly, the code that generates `THAT` is too straightforward. If you can make it better, then do so. Just don't do anything like add tests or document the code."""

import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name = 'Python Wars Solo',
    version = '1.0.3',
    description = "A retro-style Apple ][ Basic game cooked up in 45 minutes",
    license = 'GPL',
    long_description = README,
    url = 'https://github.com/pydanny/Python-Wars-Solo',
    
    author = 'Daniel Greenfeld',
    author_email = 'pydanny@gmail.com',
    
    py_modules =  ['go.py','stuff.py'],
    
    classifiers = (
        'Development Status :: 6 - Mature',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python',
    ),
)
