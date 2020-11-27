from os import listdir
from os.path import isfile, join
onlyfiles = []
dirs = []
for f in listdir("F:/"):
    if isfile(join("F:/",f)) and (f.endswith(".py") or f.endswith(".ipnb")):
        onlyfiles.append(f)
    else:
        dirs.append(f)
print(onlyfiles)
print(dirs)
# f = open("F:/Python/Tkinter/index.py",mode="r",encoding="utf-8")
# print(f.readline())