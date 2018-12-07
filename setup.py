#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
icap RESTful API
"""
from setuptools import setup, find_packages


setup(name="vlab-icap-api",
      author="Nicholas Willhite,",
      author_email='willnx84@gmail.com',
      version='2018.12.07',
      packages=find_packages(),
      include_package_data=True,
      package_files={'vlab_icap_api' : ['app.ini']},
      description="icap",
      install_requires=['flask', 'ldap3', 'pyjwt', 'uwsgi', 'vlab-api-common',
                        'ujson', 'cryptography', 'vlab-inf-common', 'celery']
      )
