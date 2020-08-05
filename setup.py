# -*- coding: utf-8 -*-
import sys
from setuptools import setup, find_packages


# keep this package private
if set(sys.argv).intersection(['upload', 'register']):
    print('This setup is private and should not be uploaded or registered.')
    sys.exit(-1)

# package settings
setup(

    # info
    name='expip',
    version='0.0.1',
    author='Alden',
    url='https://github.com/aldencolerain/expip.git',
    description='Example pip package.',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",

    # include
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,

    # public dependencies
    install_requires=[
        'pyyaml==5.3.1'],

    # keep this package private
    classifiers=['Private :: Do Not Upload'],

    # cli scripts
    entry_points={'console_scripts': ['expip = expip.cli:main']},
)
