import random
def guess_the_number(x):
    min = int(input("Enter the min value\n"))
    max = int(input("Enter the max value\n"))
    print("\n")
    n = random.randint(min,max)
    i = 0
    print("Enter the number you are thinking of")
    a = int(input())
    while(True):
        i = i + 1
        if a>n:
            print(f"Enter a number between {min} and {a}!\n\n")
            max = a

        elif a<n:
            print (f"Enter a number between {a} and {max}!\n\n")
            min = a

        else:
            print(f"{x} took {i} times to guess!")
            return i

        print("Enter the number you are thinking of")
        a = int(input())
        continue

Player1= input("Enter your name\n").capitalize()
attempt_player1 = guess_the_number(Player1)
print("\n\n")

Player2 = input("Enter your name\n").capitalize()
attempt_player2 = guess_the_number(Player2)

if attempt_player1 > attempt_player2:
    print(f"{Player2} won!")

elif attempt_player2 > attempt_player1:
    print(f"{Player1} won!")

else:
    print("Match tied")