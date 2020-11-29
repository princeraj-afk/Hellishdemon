import os

# opening file to write everything
with open("patch.txt","w") as f:

    # changing root directory
    os.chdir("D:\Hellishdemon\dealingprobs-master")

    for level1 in os.listdir():

        # if there isn't a file present in level1 folder
        try:
            for level2 in os.listdir("D:/Hellishdemon/dealingprobs-master"+"/"+level1):

                # if there isn't a file present in level2 folder
                try:
                    for level3 in os.listdir("D:/Hellishdemon/dealingprobs-master"+"/"+level1+level2):
                        k = "D:/Hellishdemon/dealingprobs-master"+"/"+level1+"/"+level2+"/"+level3

                        # getting all level3 files
                        os.chdir(k)
                        for file in os.listdir():
                            t = open(file, "r")
                            f.write(t.read())

                # if there is a file present in level2 folder
                except:
                    k = "D:/Hellishdemon/ealingprobs-master" + "/" + level1 + "/" + level2

                    # getting all level2 files
                    os.chdir(k)
                    for file in os.listdir():
                        t = open(file, "r")
                        f.write(t.read())


        # if there is a file present in level1 folder
        except:
            k = "D:/Hellishdemon/dealingprobs-master" + "/" + level1

            # getting all level1 files
            os.chdir(k)
            for file in os.listdir():
                t = open(file, "r")
                f.write(t.read())
