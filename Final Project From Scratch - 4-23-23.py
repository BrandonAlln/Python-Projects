import pickle
import time
import os
import sys



#save game, fully coded and fixed
def save_game(items,hitpoints,location,name):
    with open('gameSave.pkl','wb') as f:
        pickle.dump(items, f)
        pickle.dump(hitpoints,f)
        pickle.dump(location,f)
        pickle.dump(name,f)

#load game, fully coded and fixed
def load_game(item,hitpoints,location,name):
    with open('gameSave.pkl','rb') as f2:
        item=pickle.load(f2)
        hitpoints=pickle.load(f2)
        location=pickle.load(f2)
        name=pickle.load(f2)
        return item, hitpoints, location, name
#tutorial, fully coded and fixed
def tutorial():
    print("#__________________________________________________________________________________________________________________________________________________________#")
    print("Every Room Will Have A Prompt For You To Do Something\nPlease make sure you are typing all of your actions in lower case\nYour goal is to survive the 5 rings and complete challenges")
    print("Rooms MAY not complete if you have not found all the required items, or done the required puzzles.\nPlease Make Sure You Leave No Stone Unturned.")
    print("#__________________________________________________________________________________________________________________________________________________________#")
    time.sleep(13)
    os.system('cls')

#before game is the loop that happens when the game is first started, serving as a loading screen.
def beforeGame():
    keep_Menu = ''
    while keep_Menu != False:
        print("Welcome to Hell.....")
        print("Please Start off by saving your game...")
        print("The Default Location Will Be In Your Documents Folder")
        time.sleep(0)
        print(".....................................")
        blah = "Please Type 'start' To Continue\n"
        for l in blah:
            sys.stdout.write(l)
            sys.stdout.flush()
            time.sleep(0)
        mainmenu=input(">>>:")
        if mainmenu == 'start':
            keep_Menu == False
            break
        else:
            print("Invalid Input, Lets Try This Again...")
            time.sleep(0)
            os.system('cls')
    else:
        print("null")


#start game defines pre room 1, it changes the location of the player location variable and the player name variable
#this loop is fully coded and needs no modification
def startGame(items, hitpoints, location, name):
    os.system('cls')
    print("This is the first room, I Would Tell You What The Name Is, But Well... That Would Be Too easy....")
    print("Your first hint will be in the tutorial... that's all I can say. You have to do a little research yourself...")
    print("Try not to waste so many life points...")
    time.sleep(0)
    prompt4 = "So Adventurer...What Exactly is your name?..."
    for speaking in prompt4:
        sys.stdout.write(speaking)
        sys.stdout.flush()
        time.sleep(0)
    print(name)
    name = input("Enter A Name: ")
    print(name)
    time.sleep(0)
    prompt5 = "I see..." + str(name) + "...well...the bad news is this is clearly " + str(location) + "...but rest assured, there's a way out of here..."
    for speaking in prompt5:
        sys.stdout.write(speaking)
        sys.stdout.flush()
        time.sleep(0)
    time.sleep(0)
    os.system('cls')
    return items, hitpoints, location, name
    

    
    
#room 1 is the first room loop, I broke this up into rooms seperate from the questions that need to be asked
#fully coded and fixed with proper return statements engaged to save items.
def roomOne(items, hitpoints ,location,name): 
    print("Your Hitpoints have been established, at:", hitpoints)
    firstActive = True
    while firstActive == True:
        print("Okay", name, 'currently you are in', location, 'you need to escape....')
        print("Maybe you should start by looting that body over there...")
        print("To do so just type 'loot', 'examine' or 'exit' ")
        
        roomOnePicker = input (">>>:")

        if roomOnePicker == 'loot':
            print("You Have Obtained A Holy Sigil.")
            items.append('Holy_Sigil')
            print("You Now Have", items, "in your item bag")
            firstActive == False

        elif roomOnePicker == 'examine':
            print("I once heard that the corpse went to the party alone, because he had NOBODY to go with..")
            time.sleep(3)
            os.system('cls')
        
        elif roomOnePicker == 'exit':
            print("Exiting.....")
            time.sleep(0)
            quit()
        
        else:
            print("Invalid Input, Lets Try This Again...")
            time.sleep(0)
            os.system('cls')
    return items, location, name
            

def questionOne(items,hitpoints,location,name):
    if 'Holy_Sigil' in items:
        print("Now You Must Answer A Question To Progress To The Next Room...")
        time.sleep(0)
        os.system('cls')
        
        letsgo = True
        while letsgo == True:
            print("What is the first ring of hell called?")
            print("You May Ask For A Hint At The Cost Of Half Your Life Points..")
            print("Just type 'help' ")

            answer=input(">>>:")
            if answer == 'purgatory' or answer == 'limbo':
                print("Progressing To The Next Room...")
                break

            elif answer == 'help':
                print("The Divine Comedy References me, one name I'm a game at a party\none name I sound like the purge.")
                hitpoints = hitpoints - 50
                print("Your Hitpoints are Now,", hitpoints)
                time.sleep(10)
                os.system('cls')
                if hitpoints == 0:
                    print("You Died...")
                    time.sleep(3)
                    letsgo == False
        return items, hitpoints, location,name



        

def room2(items,location,name,hitpoints):
    pass
    






def main():
    items = []
    hitpoints = 100
    location = 'hell'
    name = 'test'
    
    
    os.system('cls')
    beforeGame()
    time.sleep(0)
    os.system('cls')
    menuChoice = True
    
    
    
    while menuChoice == True:
        print("Welcome To Hell")
        print("1. Load Game")
        print("2. Save Game")
        print("3. Start Game")
        print("4. Exit Game")
        print("5. Help Me")
        
        
        
        selection = input(">>>:")
        
        
        ##############################################################################
        #loads the game from a file that has been already saved from a previous state.
        if selection == "1":
            items, hitpoints , location ,name=load_game()
        ###############################################################################




        ###############################################################################
        #saves the game from its current state, also creates empty data file for new 
        #users, new users, please check your documents folder
        elif selection == '2':
            save_game(items,hitpoints,location,name)
            print("Saving Game...in progress...")
            time.sleep(0)
            os.system('cls')
        ###############################################################################



        #############################    Main Game Loop     ############################
        
        elif selection == '3':
            if 'Holy_Sigil' not in items:
                print("starting game...")
                items, hitpoints, location, name = startGame(items, hitpoints, location, name)
                print(items,hitpoints,location,name)
                time.sleep(0)
                roomOne(items,hitpoints,location,name)
                


            









            def hiddenfornow():
                if 'Holy_Sigil' in items:
                    questionOne()

                elif 'Holy_Sigil' in items and 'Divine_Lights' in items:
                    questionTwo()
                    time.sleep(0)
                    startGame(location,name)
                    items,hitpoints,location,name=roomOne(items,hitpoints,location,name)
            










#everything below this line is fully coded and does not need to be messed with...
        elif selection == '4':
            print("Exiting.....")
            time.sleep(3)
            quit()
        
        
        
        elif selection == '5':
            tutorial()
        
        
        
        else:
            print("Invalid Option, Please Try Another")
            time.sleep(4)
            os.system('cls')
            
    else:
        print(">>>: Incorrect Input")
        
        

main()