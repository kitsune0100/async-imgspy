# coding: utf-8
from setuptools import setup
from setuptools.command.test import test as TestCommand

import imgspy
import asyncimgspy

# Originally credited to : https://github.com/nkanaev/imgspy/tree/master
# This is a port of the repo to support asyncio
setup(
    name='async-imgspy',
    version=asyncimgspy.__version__,
    description='Find the size or type of the image without '
                'fetching the whole content.',
    long_description=asyncimgspy.__doc__,
    author='Nimit Srivastava',
    author_email='nimits4900@gmail.com',
    py_modules=['asyncimgspy'],
)
