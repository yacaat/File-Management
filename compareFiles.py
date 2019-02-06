import os
from datetime import datetime
import time
import collections
import hashlib

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

PATH = r"C:\\Users\\yalina\\Desktop\\Workspace\\"
FILE_COUNT = sum(len(files) for _, _, files in os.walk(PATH))
DASH = '-' * 40
counter = 0
print("Number of files to be checked: {}".format(FILE_COUNT))
time.sleep(1)

searchDirectories = []
searchFiles = []
searchFilesHashes = []


for root, dirs, files in os.walk(PATH):
    for dir in dirs:
        #if get_size(root + '\\' + dir) < 10000:
        searchDirectories.append(Directory(root + "\\" + dir, get_size(root + '\\' + dir)))
    for file in files:
        name = os.path.join(root, file)
        size = os.stat(name).st_size
        date = datetime.utcfromtimestamp(os.stat(name).st_mtime).strftime('%Y-%m-%d %H:%M:%S')
        searchFiles.append(File(name, size, date))
        #searchFilesHashes.append(file + str(size) + date)
        #searchFilesHashes.append(file + "-" + md5(name))
        try:
            searchFilesHashes.append((file, md5(name)))
        except Exception as e:
            print('Failed to get hash: ' + str(e))
        if len(searchFiles) % 100 == 99:
            print("%{:<3} [ {:<100} ]".format(int(100 * len(searchFiles) / FILE_COUNT), int(100 * len(searchFiles) / FILE_COUNT)*"="))
            #os.system('cls')






os.system('cls')
print("Number of files has been checked: {}".format(FILE_COUNT))
# print("Very small directories to be check:")
# print(DASH)
# print("{:<10} | {:<19}".format("Size", "Last Date"))
# print(DASH)
# for directory in searchDirectories:
#     if directory.size == 0:
#         directory.display()
#         # try:
#         #     os.rmdir(directory.name)
#         # except:
#         #     print(directory.name + "PROBLEM VAR")
#         counter = counter + 1
# print(DASH)
# print("Total: {} directories".format(counter))

# print("\nVery small files to be check:")
# print(DASH)
# print("{:<10} | {:<19} | {}".format("Size", "Last Date", "Name"))
# print(DASH)
# for file in searchFiles:
#     file.display()

# for file in searchFiles:
#     for file2 in searchFiles:
#         if file.__eq__(file2):
#             if not file.name == file2.name:
#                 file.display()
#                 file2.display()
#                 print(DASH)

hashes = []
for item in searchFilesHashes:
    hashes.append(item[1])
for i in collections.Counter(hashes).items():
    if i[1] > 1:
        for item in searchFilesHashes:
            if item[1] == i[0]:
                print(item[0])


input("\nFinished")