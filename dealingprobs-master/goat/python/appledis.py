import time
apples = int(input("Enter total no of apples\n"))
min = int(input("Enter minimum no\n"))
max = int(input("Enter maximum no\n"))
while(True):
    if min <= max:
        break
    else:
        print("Enter minimum value less than maximum")
        continue
while min<=max:
    time.sleep(1)
    if a%min == 0:
        print(f"{min} is a divisor of {apples}")
        min = min+1
        continue
    else:
        print (f"{min} is not a divisor of {apples}")
        min=min + 1
        continue