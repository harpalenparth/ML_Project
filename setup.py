from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirement(file_path:str)->List[str]:
    
    requirement=[]
    with open(file_path) as file_obj:
        requirement = file_obj.readlines()
        requirement = [req.replace('\n',' ')for req in requirement]

        if HYPEN_E_DOT in requirement:
            requirement.remove(HYPEN_E_DOT)

    return requirement

setup(
name='ml_project',
version='0.0.1',
author='parth',
author_email='xyz@gmail.com',
packages=find_packages(),
requires=get_requirement('requirement.txt')
)