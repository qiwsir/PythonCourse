#coding:utf-8

import os
from setuptools import setup, find_packages
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(name='laoqiproject',
version='1.0',
packages=find_packages(),
py_modules=['calculate'],
)