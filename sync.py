import os
from shutil import copyfile
import hashlib

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

baseFileRoot = r"C:\Users\yalina\Desktop\SenkronA"
mirrorFileRoot = r"C:\Users\yalina\Desktop\SenkronB"

for root, dirs, files in os.walk(baseFileRoot):
    for dir in dirs:
        if not os.path.isdir(os.path.join(root, dir).replace(baseFileRoot,mirrorFileRoot)):
            os.makedirs(os.path.join(root, dir).replace(baseFileRoot,mirrorFileRoot))
            print("Directory has been created. - {}".format(os.path.join(root, dir).replace(baseFileRoot,mirrorFileRoot)))
    for file in files:
        name = os.path.join(root, file)
        src = name
        dst = name.replace(baseFileRoot,mirrorFileRoot)
        if not os.path.isfile(dst):
            copyfile(src, dst)
            print("File has been created.      - {}".format(dst))
        elif md5(src) != md5(dst):
            copyfile(src, dst)
            print("File has been updated.      - {}".format(dst))


for root, dirs, files in os.walk(mirrorFileRoot):
    for dir in dirs:
        if not os.path.isdir(os.path.join(root, dir).replace(mirrorFileRoot, baseFileRoot)):
            os.rmdir(os.path.join(root, dir))
            print("Directory has been deleted. - {}".format(os.path.join(root, dir).replace(baseFileRoot,mirrorFileRoot)))
    for file in files:
        name = os.path.join(root, file)
        src = name
        dst = name.replace(mirrorFileRoot,baseFileRoot)
        if not os.path.isfile(dst):
            os.remove(src)
            print("File has been deleted.      - {}".format(dst))