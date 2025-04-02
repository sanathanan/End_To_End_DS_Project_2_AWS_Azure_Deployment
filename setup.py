from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        print(requirements)
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
name='mlproject',
version='0.0.1',
author='Sanathanan',
author_email='sanathanan.eee@gmail.com',
packages=find_packages(), # It will check for __init__.py files to build packages
# install_requires= ['pandas', 'seaborn', 'numpy'] ---> We can give like this also
install_requires=get_requirements('requirements.txt')
)