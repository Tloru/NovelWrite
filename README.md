# NovelWrite
A novel publishing platform written with Flask
# Installation
Since I'm using PyCharm and I'll probably be the only one to use this, all instructions are PyCharm Specific.  
Save all files in this repo to a folder named `Novel Write`.
open `Novel Write` in PyCharm.
Set the `Project Interpreter` to a `venv` running `Python3`.  
Install all non-`app` imports.  
In the `PyCharm Terminal`, type:  
`$ flask db init`  
Initiates the Flask database.  
`$ flask db migrate -m "users table"`   
Creates the table for all the datatypes.    
`$ flask db upgrade`  
Applies the table to the database.  
# Running
Once everything is all set, hit the run button. 
