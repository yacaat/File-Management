import os
import re
from subprocess import check_output

while True:
    r = (re.sub(r'[ıiIİ]', 'i', input("Search for:"))).lower()
    if r == "q":
        print("\n\n\n\n")
        break
    s = ""
    results = []
    for root, dirs, files in os.walk(r"C:\Users\yalina\Desktop"):
        for file in files:
            if r in (re.sub(r'[ıiIİ]', 'i', file)).lower():
                folder = root
                s = os.path.join(root, file)
                results.append(s)
    if not results:
        print("Nothing found")
    else:
        f= open("C:\\Users\\yalina\\Desktop\\" + r + "Search Result.txt", "w+", encoding="utf-8")
        for i,result in enumerate(results):
            f.write(result + "\n")
            print(str(i) + " " + result)
        f.close()

    try:
        selection = int(input("Enter the number:"))
        command = results[selection]
        check_output(command, shell=True, timeout=2)
    except:
        pass
    finally:
        os.remove("C:\\Users\\yalina\\Desktop\\" + r + "Search Result.txt")







    #   command = "explorer " + results[selection]
