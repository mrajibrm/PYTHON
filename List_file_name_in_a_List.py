# List file name in a List
import os

mypath = "/home/rajib/Documents/python/"
files_py = []
for file in os.listdir(mypath):
    if file.endswith(".py"):
        files_py.append(file)

print(files_py)