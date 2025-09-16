# Import the Libraries 

from typing import List 
from setuptools import find_packages, setup 

# Define the constant for the -e . requirement 
HYPHEN_E_DOT_REQUIREMENT = '-e .'

# create a function that will returan a list of requirements
def get_requirements(file_path: str) -> List[str]: 
    # create an empty list that will store the requirements
    requirements = []

    # Open the requirements file 
    with open(file_path) as file_obj: 
        for line in file_obj: 
            # Remove the new line character
            requirements.append(line.replace("\n", ""))
    
    # Remove the -e .
    if HYPHEN_E_DOT_REQUIREMENT in requirements: 
        requirements.remove(HYPHEN_E_DOT_REQUIREMENT)

    return requirements

setup(
    name = 'Home Electricity Bill Prediction', 
    version = '0.0.1', 
    authors = "Western", 
    author_mail = "pranjalsinha1965@gmai.com", 
    description = "This is a project to predict the home electricity bill", 
    long_description=open('README.md').read(), 
    long_description_content_type="text/markdown", 
    url="https://github.com/pranjalsinha1965/Electricity-Bill-Predictor.git", 
    license="MIT", 
    packages=find_packages(), 
    install_requires = get_requirements('requirements.txt')
)