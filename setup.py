import re
import os

from setuptools import setup, find_packages

os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.settings'

with open('abakus/__init__.py', 'r') as fd:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
        fd.read(),
        re.MULTILINE
    ).group(1)

setup(
    name="django-auth-abakus",
    version='1.1.0',
    url='http://github.com/webkom/django-auth-abakus',
    author='Webkom, Abakus Linjeforening',
    author_email='webkom@abakus.no',
    description='A django auth module that can be used to to authenticate '
                'users against the API of abakus.no.',
    packages=find_packages(exclude='tests'),
    install_requires=[
        'requests==2.7.0',
    ],
    tests_require=[
        'django>=1.4',
        'requests==2.7.0',
        'responses'
    ],
    license='MIT',
    test_suite='runtests.runtests',
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
        "Operating System :: OS Independent",
        "Natural Language :: English",
    ]
)
