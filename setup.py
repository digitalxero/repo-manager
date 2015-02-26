import os
import io
from setuptools import setup, find_packages


cwd = os.path.abspath(os.path.dirname(__file__))

with io.open(os.path.join(cwd, 'README.md'), encoding='utf-8') as fd:
    long_description = fd.read()

setup(
    name='repo_manager',
    version='0.0.1',
    description=('General purpose package repository manager that '
                 'supports plugable metadata generators, and storage backends'),
    long_description=long_description,
    url='https://github.com/Digitalxero/repo-manager',
    author='Dj Gilcrease',
    author_email='digitalxero@gmail.com',
    license='BSD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
    keywords=('createrepo'),
    packages=find_packages(),
)
