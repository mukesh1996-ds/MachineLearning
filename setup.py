from setuptools import setup, find_packages
from typing import List

PROJCT_NAME = "Machine Learning"
VERSION = "0.01"
DECRIPTION = "This our Machine Learning in Modular Coding"
AUTHOR_NAME = "Mukesh Kumar"
AUTHOR_EMAIL = "mks.mukesh1996@gmail.com"
REQUIREMENTS_FILE_NAME = "requirements.txt"
HYPHEN_E_DOT = "-e ."

# Requirements.txt file open
# read
# \n 

def get_requirements_list()->List[str]:
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n","") for requirement_name in requirement_list]
        
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list

setup(name=PROJCT_NAME,
      version=VERSION,
      description=DECRIPTION,
      author=AUTHOR_NAME,
      author_email=AUTHOR_EMAIL,
      packages=find_packages(),
      install_reqires = get_requirements_list()
     )