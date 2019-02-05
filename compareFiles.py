import os
from datetime import datetime
import time

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

  def display(self):
    print("{:<10} | {:<10} | {}".format(self.size, self.date, self.name))

def get_size(start_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

PATH = r"C:\Users\yalina\Desktop"
FILE_COUNT = sum(len(files) for _, _, files in os.walk(PATH))
DASH = '-' * 40
counter = 0
print("Number of files to be checked: {}".format(FILE_COUNT))
time.sleep(1)

searchDirectories = []
searchFiles = []


for root, dirs, files in os.walk(PATH):
    for dir in dirs:
        #if get_size(root + '\\' + dir) < 10000:
        searchDirectories.append(Directory(root + "\\" + dir, get_size(root + '\\' + dir)))
    for file in files:
        name = os.path.join(root, file)
        size = os.stat(name).st_size
        date = datetime.utcfromtimestamp(os.stat(name).st_mtime).strftime('%Y-%m-%d %H:%M:%S')
        searchFiles.append(File(name, size, date))
        if len(searchFiles) % 100 == 99:
            print("%{:<3} [ {:<100} ]".format(int(100 * len(searchFiles) / FILE_COUNT), int(100 * len(searchFiles) / FILE_COUNT)*"="))
            #os.system('cls')






os.system('cls')
print("Number of files has been checked: {}".format(FILE_COUNT))
print("Very small directories to be check:")
print(DASH)
print("{:<10} | {:<19}".format("Size", "Last Date"))
print(DASH)
for directory in searchDirectories:
    if directory.size == 0:
        directory.display()
        # try:
        #     os.rmdir(directory.name)
        # except:
        #     print(directory.name + "PROBLEM VAR")
        counter = counter + 1
print(DASH)
print("Total: {} directories".format(counter))

# print("\nVery small files to be check:")
# print(DASH)
# print("{:<10} | {:<19} | {}".format("Size", "Last Date", "Name"))
# print(DASH)
# for file in searchFiles:
#     file.display()


#
# #print(len([name for name in os.listdir(r"C:\Users\yalina\Desktop\Scripts") if os.path.isfile(name)]))
input("\nFinished")