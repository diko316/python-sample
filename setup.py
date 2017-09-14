#!/usr/bin/env python
""" Just trying to run sample.test.run() """



from distutils.core import setup

from sample import run_all

run_all()

setup(name='Sample',
      version='0.0.1',
      description='Test Python Distribution',
      author='Diko Tech Slave',
      author_email='diko316@gmail.com'
     )
