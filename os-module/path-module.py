"""
exists
isfile
isdir

split: Splits path and file name
join: Joins path and file name

basename: Returns the file name
dirname: Returns the directory path


getmtime
getattime

relpath: Returns the related path of a file or folder
abspath: Returns the absolute path of a file or folder

chdir: Changes the working directory
"""

import os
import time
existing_file = '/Users/luis.gonzalez.flores/Documents/Python Course/os-module/path-module.py'
print(os.path.exists(existing_file))
print(os.path.isfile(existing_file))
print(os.path.isdir(existing_file))
print()

print(os.path.split(existing_file))
print(os.path.join('/Users/luis.gonzalez.flores/Documents/Python Course/os-module', 'path-module.py'))
print()

print(os.path.basename(existing_file))
print(os.path.dirname(existing_file))
print()

print(time.ctime(os.path.getctime(existing_file)))
print(time.ctime(os.path.getatime(existing_file)))
print(time.ctime(os.path.getmtime(existing_file)))
print()

os.chdir('/Users/luis.gonzalez.flores/Documents/Python Course/regular-expressions')
print(os.path.relpath(existing_file))
print(os.path.abspath(existing_file))
