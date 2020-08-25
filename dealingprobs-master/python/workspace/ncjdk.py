cube = lambda x:x*x*x

def fibonacci(n):
    ar = []
    for i in range(n):
        if i==0:
            ar.append(0)
        elif i==1:
            ar.append(1)
        else:
            return fibonacci(n-1)+fibonacci(n-2)

# if __name__ == '__main__':
#     n = int(input())
#     print(list(map(cube, fibonacci(n))))
print(fibonacci(3))