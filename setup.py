# coding: utf-8

__version__ = '0.0.1'

from setuptools import setup
from setuptools.command.test import test as TestCommand

def get_requirements():
    with open('requirements.txt') as f:
        requirements = f.read().splitlines()
    return requirements

# Originally credited to : https://github.com/nkanaev/imgspy/tree/master
# This is a port of the repo to support asyncio
setup(
    name='async-imgspy',
    version=__version__,
    description='Find the size or type of the image or a list of images asychronously.',
    author='Nimit Srivastava',
    author_email='nimits4900@gmail.com',
    install_requires=get_requirements(),
    py_modules=['asyncimgspy'],
)
