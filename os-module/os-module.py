"""
os.name

os.getcwd(): Returns current working directory
os.chdir(): Changes the working directory
os.listdir(): Returns all files and folders of a given location


os.mkdir(): Creates a directory for the given path
os.mkdirs(): Creates a nested folder recursively for the given path

os.remove(): Removes a file for the given math
os.rmdir(): Removes a directory for the given math
os.removedirs(): Removes multiple directories using recursion for the given path

os.rename(): Renames a file or directory
"""

import os

print(os.name)
print(os.getcwd())
os.chdir('/Users/luis.gonzalez.flores/Documents/Python Course/regular-expressions')
print(os.getcwd())
print(os.listdir('/Users/luis.gonzalez.flores/Documents/Python Course/challenges'))
