from setuptools import setup,find_packages
from typing import List

hyphen='-e .'

def get_requirements(file_path:str)->List[str]:
     #this function will return list of requirements
    requirements=[]
    with open(file_path) as file_obj:
        requiremnts=file_obj.readlines()
        requiremnts=[req.replace("\n","")for req in requirements]

        if hyphen in requirements:
            requiremnts.remove(hyphen)

    return requiremnts



setup(
name='mlproject',
version='0.0.1',
author='Aasif',
author_email='aasifkhan47377@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')





)