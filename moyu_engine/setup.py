
#-*-coding:utf-8-*-

import sys
sys.dont_write_bytecode = True

from setuptools import find_packages, setup

setup(
    name='MoYu Engine',
    version='alpha 0.1 202306',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'moyu_engine',
    ],
)