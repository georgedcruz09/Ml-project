from setuptools import find_packages,setup
from typing import List
def get_reqirements(file_path:str)->List[str]:
    '''this function will return list of requirements '''
    hyphen='-e .'
    reqirements=[]
    with open(file_path) as file_obj:
        reqirements=file_obj.readlines()
        reqirements=[req.replace("\n","") for req in reqirements ]
        
        if hyphen in reqirements:
            reqirements.remove(hyphen) 
    
    return reqirements

setup(

    name='mlproject',
    version='0.0.1',
    author='George',
    author_email='georgedcruz1213@gmail.com',
    packages=find_packages(),
    install_requires= get_reqirements('requirement.txt')
)