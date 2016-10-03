# coding=utf-8
from distutils.core import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='matter-slash-server',
    version='0.1',
    packages=[''],
    url='dziedziul.pl',
    license='MIT License',
    author='Łukasz Dziedziul',
    author_email='l.dziedziul at gmail',
    description='Simple server handling custom Mattermost slash commands',
    install_requires=requirements,
)
