coordinates = []
for _ in range(int(input())):
    coordinates.append([int(x) for x in input().split()])
print(*(i for i in coordinates))