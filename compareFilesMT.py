import os
from datetime import datetime
import time
import collections
import hashlib
import threading

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

class Directory:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def display(self):
        print("{:<10} | {}".format(self.size,self.name))
class File:
    def __init__(self, name, size, date):
        self.name = name
        self.size = size
        self.date = date
        self.key = name + str(size) + date

    def display(self):
        print("{:<10} | {:<10} | {}".format(self.size, self.date, self.name))

    def __eq__(self, other):
        if self.name.rsplit('\\', 1)[-1] == other.name.rsplit('\\', 1)[-1] and self.size == other.size:
            return True
        else:
            return False
    # def __eq__(self, other):
    #     return self.__dict__ == other.__dict__

def get_size(start_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

def file_worker (file, root):
    name = os.path.join(root, file)
    size = os.stat(name).st_size
    date = datetime.utcfromtimestamp(os.stat(name).st_mtime).strftime('%Y-%m-%d %H:%M:%S')
    searchFiles.append(File(name, size, date))
    try:
        searchFilesHashes.append((os.path.join(root, file), md5(name)))
    except Exception as e:
        print('Failed to get hash: ' + str(e))

PATH = r"C:\Users\yalina\Desktop"
FILE_COUNT = sum(len(files) for _, _, files in os.walk(PATH))
DASH = '-' * 40
counter = 0
print("Number of files to be checked: {}".format(FILE_COUNT))
threads = []
time.sleep(1)

searchDirectories = []
searchFiles = []
searchFilesHashes = []



for root, dirs, files in os.walk(PATH):
    threads[:] = []
    for dir in dirs:
        searchDirectories.append(Directory(root + "\\" + dir, get_size(root + '\\' + dir)))
    for file in files:
        t = threading.Thread(target=file_worker,args=(file, root))
        t.start()
        threads.append(t)
        if len(searchFiles) % 100 == 99:
            print("%{:<3} [ {:<100} ]".format(int(100 * len(searchFiles) / FILE_COUNT), int(100 * len(searchFiles) / FILE_COUNT)*"="))
    for t in threads:
        t.join()







os.system('cls')
print("Number of files has been checked: {}".format(FILE_COUNT))
hashes = []
for item in searchFilesHashes:
    hashes.append(item[1])
for i in collections.Counter(hashes).items():
    if i[1] > 1:
        for item in searchFilesHashes:
            if item[1] == i[0]:
                print(item[0])



input("\nFinished")