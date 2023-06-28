import os
 
counter = 0
contains = 0
path = "/Users/matthew_gu/Desktop/1/pythons"
for filename in os.listdir(path):
    if filename.endswith(".py"):
        f = os.path.join(path, filename)
        # checking if it is a file
        if os.path.isfile(f):
            counter += 1
            with open(f) as a:
                code = a.read()
            if "input" in code.split("def main")[1]:
                contains += 1 
            else:
                print(f)



print(contains/counter)
