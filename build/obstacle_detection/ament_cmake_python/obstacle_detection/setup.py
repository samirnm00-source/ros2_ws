from setuptools import find_packages
from setuptools import setup

setup(
    name='obstacle_detection',
    version='0.0.1',
    packages=find_packages(
        include=('obstacle_detection', 'obstacle_detection.*')),
)
