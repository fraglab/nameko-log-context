#!/usr/bin/python
# -*- coding: utf-8 -*-
from setuptools import setup

__version__ = '0.0.3'

setup(
    name='nameko-log-context',
    version=__version__,
    author='Maxim Kiyan',
    author_email='maxim.k@fraglab.com',
    url='https://github.com/fraglab/nameko-log-context',
    description='worker_ctx custom fields logging',
    py_modules=['nameko_log_context'],
    install_requires=['nameko>=2.0.0']
)
