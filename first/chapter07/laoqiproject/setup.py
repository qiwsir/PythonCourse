#coding:utf-8
from setuptools import setup, find_packages

setup(
    name='laoqiproject', 
    version='0.1.1',
    keywords=('setup', 'laoqi'),
    description='an example of publishing to pypi',
    long_description='',
    license='MIT', 
    install_requires=[], 
    author='qiwsir',
    author_email='qiwsir@qq.com',
    packages=find_packages(), 
    platforms='any',
    url='https://github.com/qiwsir/PythonCourse/tree/master/first/chapter07/laoqiproject', 
    include_package_data = True,
    # entry_points={
    #     'console_scripts':[
    #         'example=run:main' 
    #     ]
    # },
)     