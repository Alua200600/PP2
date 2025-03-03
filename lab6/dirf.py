#Task1
from pathlib import Path
path = Path(input("Enter directory path: ").strip())  
if not path.exists():
    print("Don't found")
else:
    directories = [d.name for d in path.iterdir() if d.is_dir()]
    files = [f.name for f in path.iterdir() if f.is_file()]
    all_items = [item.name for item in path.iterdir()]
    print("Directories:", directories)
    print("Files:", files)
    print("All items:", all_items)

#Task2
import os
p = input("Enter the path: ").strip()
if os.path.exists(p):
    print("Path exists!")
    print("Readable:", "Yes" if os.access(p, os.R_OK) else "No")
    print("Writable:", "Yes" if os.access(p, os.W_OK) else "No")
    print("Executable:", "Yes" if os.access(p, os.X_OK) else "No")
else:
    print("Path not found")

#Task3
path = input("Enter the path: ").strip()
if os.path.exists(path):
    print("Path exists!")
    directory = os.path.dirname(path)
    print("Directory:", directory)
    filename = os.path.basename(path)
    print("Filename:", filename)
else:
    print("Path does not exist")

#Task4
file_path = input("Path: ").strip()
if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        line_count = sum(1 for _ in file)
    print(f"num_of_lines: {line_count}")
else:
    print("Don't found")

#Task5
my_list = ["Apple", "Banana", "Cherry", "Mango"]
file_path = input("Enter the file path: ").strip()
with open(file_path, "w") as file:
    for item in my_list:
        file.write(item + "\n") 
print("List successfully written to the file")

#Task6
import string
for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", "w") as file:
        file.write(f"This is {letter}.txt\n")
print("26 txt files created")

#Task7
f1 = input("Path1: ").strip()
f2 = input("Path2: ").strip()
with open(f1, "r") as src, open(f2, "w") as dest:
    dest.write(src.read()) 
print(f" {f1} copied to {f2} ")

#Task8
f = input("file path to delete: ").strip()
if os.path.exists(f):
        os.remove(f) 
        print(f"{f} is deleted")
else:
    print(f"{f} does not exist.")







