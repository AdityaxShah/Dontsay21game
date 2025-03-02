def nearestMultiple(num):
    if num >= 4:
        near = num + (4 - (num % 4))
    else:
        near = 4
    return near

def lose1():
    print("\n\nYOU LOSE!")
    print("Better luck next time!")
    exit(0)

def check(xyz):
    for i in range(1, len(xyz)):
        if xyz[i] != xyz[i - 1] + 1:
            return False
    return True

def start1():
    xyz = []
    num = 0
    print("\nYou can start by saying up to 3 numbers in increasing order.")
    print("For example: 1, 2, 3\nThe one who says '21' loses!")

    chance = input("\nDo you want to take the first chance? (Y/N): ").strip().upper()

    if chance == "Y":
        while num < 20:
            inp = int(input("\nHow many numbers will you say? (1-3): "))
            if 1 <= inp <= 3:
                comp = 4 - inp
            else:
                print("Wrong input! You are disqualified from the game.")
                lose1()

            print("Now enter the values:")
            for _ in range(inp):
                xyz.append(int(input("> ")))

            last = xyz[-1]

            if check(xyz):
                if last == 21:
                    lose1()
                else:
                    for j in range(1, comp + 1):
                        xyz.append(last + j)
                    print("\nOrder of inputs after computer's turn: ")
                    print(xyz)
                    last = xyz[-1]
            else:
                print("\nYou did not input consecutive integers.")
                lose1()

    elif chance == "N":
        print("\nComputer starts...")
        comp = 1
        last = 0
        while last < 22:
            for j in range(1, comp + 1):
                xyz.append(last + j)
            print("\nComputer says:", xyz[-comp:])

            last = xyz[-1]
            if last == 21:
                print("\nComputer lost! You win! 🎉")
                exit(0)

            inp = int(input("\nHow many numbers will you say? (1-3): "))
            if 1 <= inp <= 3:
                print("Now enter the values:")
                for _ in range(inp):
                    xyz.append(int(input("> ")))

                last = xyz[-1]

                if not check(xyz):
                    print("\nYou did not input consecutive numbers!")
                    lose1()
            else:
                print("\nInvalid choice! You lose!")
                lose1()
    else:
        print("\nInvalid choice! Exiting game...")

print("\nDo you want to play the 'Don't Say 21' game? (Yes / No)")
ans = input("> ").strip().capitalize()
if ans == 'Yes':
    start1()
else:
    print("Do you want to quit the game? (Yes / No)")
    nex = input("> ").strip().lower()
    if nex == "yes":
        print("You are quitting the game...")
        exit(0)
    elif nex == "no":
        print("Continuing...")
    else:
        print("Wrong choice! Exiting...")
