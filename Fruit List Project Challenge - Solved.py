def countlines():
    with open("FruitList.txt") as file:
        lines = file.readlines()
        total_lines = len(lines)
        return total_lines





try:
    count = 0
    fileOpen = open("FruitList.txt", "r")
    print("The Total Lines In File:", countlines())
    userchoice = int(input("enter a number to select line: "))
    for line in fileOpen:
        if count == userchoice:
            print("You Selected", count ,line)
        count+=1
        if userchoice > 7:
            print("That is not a valid Choice, Chose 0-7")
            break
except FileNotFoundError as err:
    print("This file does not exist",err)


    #challenge, how could I make this work with any file, I don't know how many lines.
    #Challenge has been solved in challenge countlies.

