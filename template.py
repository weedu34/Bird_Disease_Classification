#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
from pathlib import Path
import logging


# In[ ]:


logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


# In[ ]:


project_name = 'cnnClassifier'


# In[ ]:


files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]


# In[ ]:


for file_path in files:
    filepath = Path(file_path) # for creating path of all files in the files list
    file_dir, file_name = os.path.split(filepath)
    
    if file_dir !="":  # creating file directories of all files in the files list if not exists
        os.makedirs(file_dir,exist_ok=True)
        logging.info(f"creating directory:{file_dir}, for the ´file: {file_name}")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
            logging.info(f"Creating file:{filepath}")
    else:
        logging.info(f"{file_name} is already exists")
        
        

