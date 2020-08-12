# quiz
# create a co-routines that takes input from user and return the file name
# from 15 letters in which it is present or not

def name_search():
    print("Reading...")

    f1 = open("grtf.py", 'r')   # a+ creates the file if not exist
    f2 = open("aryyan.py", 'r')   # a+ lets appending data not overriding previous
    f3 = open("healthy programmer.py", 'r')   # a+ also let us to read
    f4 = open("gadgets.py", 'r')
    z1 = f1.read()
    z2 = f2.read()
    z3 = f3.read()
    z4 = f4.read()

    while True:
        text = (yield)
        if text in z1:
            print("found in letter 1.txt")
        elif text in z2:
            print("found in letter 2.txt")
        elif text in z3:
            print("found in letter 3.txt")
        elif text in z4:
            print("found in letter 4.txt")
            f1.close()
            f2.close()
            f3.close()
            f4.close()
            print("Closed all files")
        else:
            print("not found")


search = name_search()
next(search)
while True:
    x = input("Enter a Name to search in letters or quit : ")
    if x == "quit":
        print("Quiting...")
        search.send("close")
        break

    else:
        search.send(x)