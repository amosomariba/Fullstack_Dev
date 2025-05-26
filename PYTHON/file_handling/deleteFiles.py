import os

if os.path.exist("sample.txt"):
    os.remove("sample.txt")

else:
    print("Sorry file does not exist")
