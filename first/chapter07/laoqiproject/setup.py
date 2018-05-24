# 引用包管理工具setuptools，其中find_packages可以帮我们便捷的找到自己代码中编写的库
from setuptools import setup, find_packages

setup(
    name='laoqiproject', 
    version='0.1',
    keywords=('setup', 'laoqi'),
    description='an example of publishing to pypi',
    long_description='',
    license='MIT', 
    install_requires=[], 
    author='qiwsir',
    author_email='qiwsir@qq.com',
    packages=find_packages(), 
    platforms='any',
    url='' 
    include_package_data = True,
    entry_points={
        'console_scripts':[
            'example=run:main' 
        ]
    },
)