import os

print(os.getcwd())

os.chdir("C:\\Users\\jblomer\\Desktop\\")

print(os.getcwd())
for dirpath, dirnames, filenames in os.walk("C:\\Users\\jblomer\\Desktop\\DataSamples\\"):
    print("Current path: ", dirpath)
    print("Directories: ", dirnames)
    print("Files: ", filenames)
    print("num of files: ", filenames.__len__())
    print()