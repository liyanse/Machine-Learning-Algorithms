## Finding files with .sol extesion and moving them into another folder
import os
import shutil

print("Contents of the source and destination before moving")

source = r"C:\Users\LENOVO\Desktop\Solidity-DocGen\data\learning-solidity\49_UUPS"
destination = r"C:\Users\LENOVO\Desktop\Solidity-DocGen\data\learning-solidity"

for root, dir, files in os.walk(source):
    print(root)
    print(dir)
    print(files)
    
##contents of the source path before moving
print(os.listdir(destination))

##moving the solidity files
for root, dir, files in os.walk(source):
    for file in files:
        if ".sol" in file:
            shutil.move(os.path.join(root, file), destination)
            
            
#contents of directories after moving files
print("Contents of destination files after moving")

#contents of destination path after moving solidity files
print(os.listdir(destination))
