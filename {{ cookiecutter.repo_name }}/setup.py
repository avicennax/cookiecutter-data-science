# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name='{{ cookiecutter.package_name }}',
    version='0.1.0',
    author='{{ cookiecutter.author_name }}',
    author_email='{{ cookiecutter.author_email }}',
    packages=['{{ cookiecutter.package_name }}'],
    license='{{ cookiecutter.open_source_license }}',
    description='{{ cookiecutter.description }}',
    long_description=open('README.md').read(),
    install_requires=open('requirements.txt').read().split('\n')[:-1]
)
