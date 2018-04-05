# coding:utf8
from setuptools import setup, find_packages

setup(
    name='easyutils',
    version='0.1.7',
    packages=find_packages(),
    description='A utility for China Stock',
    author='shidenggui',
    author_email='longlyshidenggui@gmail.com',
    license='BSD',
    url='https://github.com/shidenggui/easyutils',
    keywords='China stock trade',
    install_requires=['requests', 'pyquery'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'License :: OSI Approved :: BSD License'
    ],
)
