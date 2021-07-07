# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 09:56:10 2021

@author: alejo
"""

d = {
    "dependencies": {
       "numpy": "^1.21.0",
       "pandas": "^1.2.5"
         }
    }


with open("requirements.txt", "w+") as f:
   for i,j in zip(d["dependencies"].keys(), d["dependencies"].values()):
       line = "{}=={}\n".format(i, j.strip("^"))
       f.writelines(line)