import os

from setuptools import setup
from setuptools import find_packages

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.rst')).read()
except IOError:
    README = ''
try:
    CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()
except IOError:
    CHANGES = ''

version = '1.0.1'

install_requires = [
    'click>=6.6',
    'Kotti>=1.0.0',
    'kotti_tinymce',
    'progress'
]


setup(
    name='kotti_toolkit',
    version=version,
    description="Utilities for Kotti",
    long_description='\n\n'.join([README, CHANGES]),
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "License :: Repoze Public License",
    ],
    author='Oshane Bailey',
    author_email='b4.oshany@gmail.com',
    url='https://github.com/Collective-Kotti/kotti_toolkit',
    keywords='kotti tools utils web cms wcms pylons pyramid',
    license="BSD-derived (http://www.repoze.org/LICENSE.txt)",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    tests_require=[],
    dependency_links=[],
    entry_points={
        'console_scripts': [
            'new-site = kotti_toolkit.scripts.importer:new_site',
            # Users and groups
            'create-user = kotti_toolkit.scripts.importer:create_user'
        ]
    },
    extras_require={},
)
