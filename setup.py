# coding: utf8

from setuptools import setup, find_packages

setup(
    name='Flask-Gist',
    version='0.1.0',
    license='MIT',
    description='A simple flask extension to render Github Gists on template',
    long_description=open('README.md').read(),
    author='Ellison Leão',
    author_email='ellisonleao@gmail.com',
    url='https://github.com/ellisonleao/Flask-Gist/',
    platforms='any',
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    install_requires=['Flask'],
    packages=find_packages()
)
