from typing import List
from setuptools import find_packages
from distutils.core import setup

def get_requirements():
    requirement_list:List[str]=[]
    with open('requirements.txt') as f:
        for line in f.readlines():
            requirement_list.append(line.strip())
            
    return requirement_list
setup(
    name="sensor",
    version="0.0.1",
    author="Shubham",
    author_email="shubhamgupta2048@gmail.com",
    packages=find_packages(),
    install_requires=[],
)