#all needed imports
import pickle
import time
import os
import sys
import random

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

#tutorial for those playing the game            
def tutorial():
    print("#__________________________________________________________________________________________________________________________________________________________#")
    print("Every Room Will Have A Prompt For You To Do Something\nPlease make sure you are typing all of your actions in lower case\nYour goal is to survive the 5 rings and complete challenges")
    print("Rooms MAY not complete if you have not found all the required items, or done the required puzzles.\nPlease Make Sure You Leave No Stone Unturned.           ")
    print("PLEASE SAVE YOUR GAME REGULARLY, IF YOU DIE AND ENCOUNTER LOADING ERRORS TRY DELETING YOUR SAVEGAME, SEARCH YOUR PC FOR A .pkl EXTENSION AND REMOVE IT      ")
    print("==================================================After That, Try Running The Game==========================================================================")
    print("#__________________________________________________________________________________________________________________________________________________________#")
    time.sleep(20)
    os.system('cls')

#custom ascii title screen
def title_screen():
    print("""
    
    
    
    """)
    print("                                                                                                                             ███████╗░██████╗░█████╗░░█████╗░██████╗░███████╗  ██╗░░██╗███████╗██╗     ██╗")
    print("                                                                                                                             ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝  ██║░░██║██╔════╝██║░░░░░██║")
    print("                                                                                                                             █████╗░░╚█████╗░██║░░╚═╝███████║██████╔╝█████╗░░  ███████║█████╗░░██║░░░░░██║")
    print("                                                                                                                             ██╔══╝░░░╚═══██╗██║░░██╗██╔══██║██╔═══╝░██╔══╝░░  ██╔══██║██╔══╝░░██║░░░░░██║")
    print("                                                                                                                             ███████╗██████╔╝╚█████╔╝██║░░██║██║░░░░░███████╗  ██║░░██║███████╗███████╗███████╗")
    print("                                                                                                                             ╚══════╝╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░░░░╚══════╝  ╚═╝░░╚═╝╚══════╝╚══════╝╚══════╝")
    print("""
                                                                                                                                              ._                                            ,
                                                                                                                                              (`)..                                    ,.-')
                                                                                                                                               (',.)-..                            ,.-(..`)         
                                                                                                                                               (,.' ,.)-..                    ,.-(. `.. )                    
                                                                                                                                                (,.' ..' .)-..            ,.-( `.. `.. )                     
                                                                                                                                                 (,.' ,.'  ..')-.     ,.-( `. `.. `.. )                      
                                                                                                                                                  (,.'  ,.' ,.'  )-.-('   `. `.. `.. )                       
                                                                                                                                                   ( ,.' ,.'    _== ==_     `.. `.. )                        
                                                                                                                                                    ( ,.'   _==' ~  ~  `==_    `.. )                     
                                                                                                                                                    \  _=='   ----..----  `==_   )                     
                                                                                                                                                ,.-:    ,----___.  .___----.    -..                        
                                                                                                                                            ,.-'   (   _--====_  \/  _====--_   )  `-..                 
                                                                                                                                        ,.-'   .__.'`.  `-_I0_-'    `-_0I_-'  .'`.__.  `-..     
                                                                                                                                    ,.-'.'   .'      (          |  |          )      `.   `.-..  
                                                                                                                                ,.-'    :    `___--- '`.__.    / __ \    .__.' `---___'    :   `-..      
                                                                                                                              -'_________`-____________'__ \  (O)  (O)  / __`____________-'________`-     
                                                                                                                                                         \ . _  __  _ . /                               
                                                                                                                                                          \ `V-'  `-V' |                                 
                                                                                                                                                           | \ \ | /  /                                 
                                                                                                                                                            V \ ~| ~/V                                   
                                                                                                                                                             | \  /|                                    
                                                                                                                                                              \~ | V                                 
                                                                                                                                                               \  |                                        
                                                                                                                                                                VV
    """)
    time.sleep(5)
    os.system('cls')
    time.sleep(1)

#loading screen for fun, modified published code (for fun credited source)
def loading_screen():
    import time
    import os
    import sys
    os.system('cls')

    bar = [
        " [=     ]loading...",
        " [ =    ]loading...",
        " [  =   ]loading...",
        " [   =  ]loading...",
        " [    = ]loading...",
        " [     =]loading...",
        " [    = ]loading...",
        " [   =  ]loading...",
        " [  =   ]loading...",
        " [ =    ]loading...",
    ]
    i = 0
    total = 0
    while total != 30:
        print(bar[i % len(bar)], end="\r")
        time.sleep(.2)
        i += 1
        total += 1
        os.system('cls')

    #improved upon loading screen from Stack Overflow 
    #updated iteration to stop at 30 cycles using a accumulating sentinel...
    #did this for giggles and fun :)
    #source and credit to
    #answered Oct 25, 2019 at 9:06
    #LPby
    #https://stackoverflow.com/questions/7039114/waiting-animation-in-command-prompt-python

#first room initiation
def roomOne(items, hitpoints, location, name):
    if 'Holy_Sigil' not in items:
        location = 'Hell'
        print("Hello Adventurer..What is Your name?")
        name=input(">>>: ")
        time.sleep(2)
        print("Nice to meet you...", name)
        time.sleep(1)
        print("Your Current Location is", location, "your hitpoints are:", hitpoints)
        print("You Enter The Room, Which Way Would You Like to go..")
        print("You Have 4 Ways To Go, Look For An Item...")
        
        #while loop that returns updated variable, Holy_Sigil Will Move To The question prompt function. Thus has an interaction.
        while 'Holy_Sigil' not in items:
            print("'north, south, east, west'")
            playerInput=input(">>>: ")
            if playerInput == 'north':
                items.append("Holy_Sigil")
                print("You have found the holy sigil!")

            #You take damage from fire updating hitpoints
            elif playerInput == 'south':
                print("You Burn Yourself on some fire")
                hitpoints -= 5
                print("Current Hitpoints", hitpoints)
                time.sleep(2)
            
            #Nothing Happens, Empty Area
            elif playerInput == 'east':
                print("You Find Literally Nothing here of use...")
                time.sleep(2)
            
            #Useless Body
            elif playerInput == 'west':
                print("You Find A Body....I Don't Think He's moving any time soon...")
                time.sleep(2)
            
            #checks to see if player just kept eating fire
            elif hitpoints<=0:
                print("You Died")
                quit()
            #handles invalid input
            else:
                print("Please Choose A Valid Location..")
                time.sleep(2)
        
        #returns updated variables
        return  items,hitpoints,location,name
    
    #bug test code for loads
    else:
        print("Holy Sigil is in items, check for prompt.")

#propts question one for room one     
def questionOne(items, hitpoints, location, name):
    #updates to new location
    location = 'questionOne'
    #checks to make sure player isn't dead (load catch) and that they obtained the proper item to initate the loop.
    if hitpoints >=0 and 'Holy_Sigil' in items:
        loopTrue = True
    #trivia loop that breaks when loopTrue == False.
        while loopTrue == True:
            print('Items in inventory',items,"Hitpoints",hitpoints, "location",location, "player name", name)
            print("The Sigil Glows Bright.")
            print("Before You Enter The next room you must answer some trivia...")
            time.sleep(1)
            print("What is the first ring of hell called?")
            print("You May Ask For A Hint At The Cost Of Half Your Life Points..")
            print("Just type 'help'...or you can type 'quit to quit the game' ")

            answer=input(">>>:")

            #checks to see if the player died and closes out their game.
            if hitpoints <= 0:
                    print("You Died...")
                    time.sleep(0)
                    quit()
            
            #correct answer condition that moves to the next room, takes a boolean answer as a string.
            if answer == 'purgatory' or answer == 'limbo':
                print("Progressing To The Next Room...")
                print(hitpoints)
                loopTrue = False
                return items,hitpoints,location,name
            
            #quits the game optionally
            elif answer == 'quit':
                print("quitting game...")
                time.sleep(0)
                quit()
            #gives the player a hint at the puzzle
            elif answer == 'help':
                print(hitpoints)
                print("The Divine Comedy References me, one name I'm a game at a party\none name I sound like the purge.")
                hitpoints -= 50
                print(hitpoints)
                print("Your Hitpoints are Now,", hitpoints)
            
            #handles incorrect input
            else:
                print("Wrong... Try Again...")
                time.sleep(0)

#room two is a fight room against a random low level demon
def roomTwo(items, hitpoints, location, name):
    #sets location to new room
    location = 'roomTwo'
    print("Welcome to the second ring of hell\nThere might be something for you to find in here...")
    time.sleep(2)
    
    #Tutorial for room
    print("The Controlls are the exact same as I mentioned before....")
    print(" 'north', 'south', 'east', 'west', but now we have 'save' and 'exit'")
    
    #checks to see if item is in list to initiate the room
    if 'Holy_Sigil' in items:
        userInput = ''
        while userInput != 'exit':
            
            #user input
            userInput=input(">>>:")
            
            #exits the game
            if userInput == 'exit':
                print("Exiting Game, Without Saving...")
            
            #saves the game
            elif userInput == 'save':
            
                save_game(items, hitpoints, location, name)
            
            #condition area for boss fight
            elif userInput == 'west':
                
                #defines stats for player and the demon
                you_attack = 0
                demon_health = 100
                demon_attack = 0
                
                #demon fight conditional while loop
                while hitpoints > 0 and demon_health > 0:
                 # you attack demon
                    you_attack = random.randint(10, 20)
                    demon_health-=you_attack
                    print("You attack the demon for", you_attack, "damage. demon has", demon_health, "health left.")
                    time.sleep(2)

                    demon_attack = random.randint(1,10)
                    hitpoints -= demon_attack
                    print("demon attacks you for", demon_attack, "damage. You have", hitpoints, "health left.")
                    time.sleep(2)
                    
                    
                    # Checks to see if the player is dead and saves the game.
                    if hitpoints <= 0:
                        print("You Have Died Demon wins!")
                        save_game(items,hitpoints,location,name)
                        quit()
                
                   #Winning Loop For Demon Killed, A bit buggy, but if you do everything correctly it works as intended.
                    elif demon_health <= 0:
                        print("YOU HAVE KILLED THE DEMON")
                        items.append('Divine_Light')
                        print("You now have", items, "In Your Backpack!")
                        print("The east door opens and you exit into a new room....")
                        return items, hitpoints, location, name
                
            
            #dead room with nothing in it
            elif userInput == 'north':
                print("There seems to be a whole lot of nothing this way...")
                print("Maybe try a different way....")
                print(" 'north', 'south', 'east', 'west','save','exit'")

            #south room that gives you some minor damage, because I said so of course.
            elif userInput == 'south':
                print("You Take Damage, because I said so...")
                hitpoints-=5
                print(hitpoints)
                print(" 'north', 'south', 'east', 'west','save','exit'")

            #item boost that helps kill satan in the end
            elif userInput == 'east':
                print("There's a door here...")
                time.sleep(1)
                print("you open it...")
                time.sleep(1)
                print("You find an amulet...")
                time.sleep(1)
                
                #adds item to the list
                items.append('Amulet_Of_Fury')
                time.sleep(0)
                print("You Now Have,", items, "in your backpack")
                print(" 'north', 'south', 'east', 'west','save','exit'")
            
            #handles incorrect input
            else:
                print("invalid input, please check spelling...")
    
    #beautiful bug code, zap goes the bug.
    else:
        print("How did you get in here? Stop Exploiting Bugs Please.")
        quit()

#room three is a fight room against cerberus
def roomThree(items, hitpoints, location, name):
    time.sleep(1)
    #sets the location of the room
    location = 'Gluttony'
    
    #checks to see if Amulet and Divive Light are in items, demon is a mandatory kill to exit the room.
    if 'Amulet_Of_Fury' in items and 'Divine_Light' in items:
        print("You Have Entered The Third Circle Of Hell.")
        time.sleep(1)
        print("It reaks of rotten flesh...")
        time.sleep(1)
        print("You should start by exploring the room again...")
        
        #initializes the loop
        userInput = ''
        
        #menu system for the room
        while userInput != 'exit':
            print(" 'north', 'south', 'east', 'west', 'save' and 'exit', type 'showstats' to see your current stats...")
            userInput=input(">>>:")
            if userInput == 'showstats':
                print("Player Name:",name,"\nCurrent Items In Inventory:", items,"\nCurrent Hitpoints:",hitpoints,"\nCurrent Location",location)
            elif userInput == 'save':
                save_game(items,hitpoints,location,name)
                print("Game has been saved...")
                time.sleep(1)
            
            #quits the game
            elif userInput == 'exit':
                print("exiting")
                time.sleep(1)
                quit()
            
            #Bonus Health Room with Mandatory Item To Slay Cerberus
            elif userInput == 'east':
                hitpoints += 1000
                print("Your HitPoints Have Been Sanctified By Gods Grace..current hitpoints...", hitpoints)
                items.append('God_Slayer_Scythe')
                print("You have obtained the God Slayer's Scythe...")
                print(items)
                print("You're Going To Need This....")
            
            #hell lore room location
            elif userInput == 'north':
                print("You Witness The Gluttons in their domain...they scarf down flesh like pigs...")
                print("They hardly look human anymore....","It's best for now that you keep moving forward...")
            
            #make sure you check the other rooms prompt
            elif userInput == 'south':
                print("You come acorss cerberus....you should check around to make sure you can get a good attack in..")
                print("You should also look around for better items.....")
            
            #Cerberus Room Condition and Fight, Reused Demon Code.
            elif userInput == 'west':
                    print("Cerberus Snarles at you...")
                    time.sleep(3)
                    if 'God_Slayer_Scythe' in items:
                        playerDamage = 0
                        cerberusAttack = 0
                        cerberusHealth = 500
                        while hitpoints >= 0 and cerberusHealth >= 0:
                    
                            playerDamage = random.randint(100, 150)
                            cerberusHealth-=playerDamage
                            print("You attack Cerberus for", playerDamage, "damage. Cerberus has", cerberusHealth, "health left.")
                            time.sleep(0)

                            cerberusAttack = random.randint(40,50)
                            hitpoints -= cerberusAttack
                            print("Cerberus Attacks you for", cerberusAttack, "damage. You have", hitpoints, "health left.")
                            time.sleep(0)
                            
                            
                            # Checks to see if the player is dead and saves the game.
                            if hitpoints <= 0:
                                print("CERBERUS CRUSHES YOUR HEAD INTO THE BASE OF YOUR SPINE")
                                print("YOU'RE DEAD")
                                save_game(items,hitpoints,location,name)
                                quit()
                        
                            #checks if cerberus is dead and moves you to another room if he is. or she? I don't know it's a three headed demon dog.
                            elif cerberusHealth <= 0:
                                print("CERBERUS HAS BEEN SLAIN")
                                time.sleep(2)
                                items.append('Cerberus_Heads')
                                print("You now have", items, "In Your Backpack!")
                                hitpoints+=1000
                                print("Hitpoints:", hitpoints)
                                time.sleep(2)
                                print("You Move On Past Cerberus...Deeper into hell..")
                                time.sleep(2)
                                return items, hitpoints, location, name
                    
                    #handles incorrect items in list, does not allow room to start, makes you quit.
                    else:
                        print("You did not come prepared to this fight....")
                        print("You fight cerberus bare handed and have your head torn from your torso..")
                        save_game(items, hitpoints, location, name)
                        time.sleep(3)
                        quit()
            
            #handles incorrect input
            else:
                print("invalid choice")
        
        #handles potential bugs
        else:
            print("test: report this bug")
    
    #does not allow the room if the conditions are not met
    else:
        print("You do not have the correct item for this room...\nexiting program....")

#room four is mostly a quiz room with a single health boost in one of the rooms.
def roomFour(items, hitpoints, location, name):
    time.sleep(3)
    #location is set
    location = 'avarice'
    print("You have entered the fourth circle of hell...")
    print("ahhh...", location, "Where those who horde wealth end up burning in the own fine medals..")
    print("You should start by exploring the room.")
    #Checks to see if the proper item is in the list and runs the next lines if it is.
    if 'Cerberus_Heads' in items:
        userInput = ''

        #a massive amount of nested loops for ultra engaging experience. My fingers are hurting from commenting and typing so much code Vlad.. I appriciate brown switch mechanical keyboards alot now.
        while userInput != 'exit':
            print("'north','south','east','west', and 'save', You can also type 'showstats' to see your current stats...")
            userInput = input(">>>:")
            #nested menu system that allows the user to navigate the room.
            #also some lore about this ring of hell is displayed.
            if userInput == 'north':
                print("You examine the 4th ring of avarice, this is also known as the ring of greed...")
                print("Lets hope your choices aren't too greedy...")
                print("You walk around aimlessly looking for anything, you can't seem to find anything...")
            
            #nothing happens!
            elif userInput == 'east':
                print("You find nothing of value.... try another direction...")
            
            #Hitpoint secret boost room, I left this for plenty of reiterations, helpful to debug.
            elif userInput == 'west':
                hitpoints+=10000000
                print("Hitpoint Boost! Your hitpoints are now:", hitpoints)
           #saves the game
            elif userInput == 'save':
                save_game(items,hitpoints,location,name)
            
            #shows your current stat variables 
            elif userInput == 'showstats':
                print("Player Name:",name,"\nCurrent Items In Inventory:", items,"\nCurrent Hitpoints:",hitpoints,"\nCurrent Location",location)
            
            #south room instance is initialized.....
            elif userInput == 'south':
                #while loop that runs until the user is dead or if they answer the questions correctly this should be no problem....
                while hitpoints != 0:
                    print("Who is Dante's Guide and Mentour in the Divine Comedy?")
                    holyChoice = input(">>>: ")
                    #more nested trivia
                    if holyChoice == 'virgil':
                        print("Correct.")
                        print("How many circles are in the divine comedy?")
                        circleGuess = input(">>>:")
                        #more nested trivia
                        if circleGuess == '7' or circleGuess == 'seven':
                             items.append('Final_Key')
                             print("You have placed the Final_Key in your inventory, the next room is opening for you....")
                             return items, hitpoints, location, name
                            #finally end of the loop shatter and return
                        
                        #calculates damage if question is wrong
                        else:
                         print("Incorrect...you attone for your sins...")
                         hitpoints-=30
                         print("your hitpoints are", hitpoints, "try again....")
                         
                         #validator for another way of saying get good.
                         if hitpoints <= 0:
                             print("Game ending..you died...")
                             quit() 
                             #makes you leave my game for sucking this bad.

                    #calculates damage if question is wrong             
                    else:
                         print("Incorrect...you attone for your sins...")
                         hitpoints-=30
                         print("your hitpoints are", hitpoints, "try again....")
                         if hitpoints <= 0:
                             print("Game ending..you died...")
                             quit()
            else:
                print("invalid input...")                 
    
    #Else statement for heads if they do not exist and breaks the loop
    else:
        print("You Need To Defeat Cerberus To Be Able to Enter this room...")
        return

#room five is a prebossfight room that has multiple items inside for the player to power up with
def roomFive(items, hitpoints, location, name):
        location = 'roomFive'
    #looks to see if final boss key is in the items list

        if 'Final_Key' in items or 'Cerberus_Heads':
            #changes the location variable to putrid marsh
            location = 'putrid marsh'
            print("Welcome to the fifth ring of hell. This room is the,", location)
            print("Your best advised to look for everything in this room to enter the boss room...")
            #while loop initializer

            userChoice = ''

            #while loop that allows users to move about freely

            while userChoice != exit:
                print("Your Directions: 'north', 'south', 'east', 'west', 'save' ' 0 = exit'")
                userChoice = input(">>>: ")

                if userChoice == 'north':

                    #adds Satans Bane power up to list
                    items.append('Satans_Bane')
                    print("You have obtained Satans_Bane, your current items are", items)

                #exits the program and userChoice ends
                elif userChoice == '0':
                    print("Exiting program...")
                    quit()

                #saves the game and calls for save(pickle) to convert items to binary.
                elif userChoice == 'save':
                    save_game(items, hitpoints, location, name)
                    pass

                #adds draconic claw power up to items list
                elif userChoice == 'south':
                    items.append('Draconic_Claw')

                    #increases hitpoints for final boss fight
                    hitpoints += 10000

                    #shows player stats
                    print("your hitpoints are now", hitpoints,
                        "You have obtained a boost...draconic claw...")
                #input east option
                elif userChoice == 'east':
                    #adds item to list
                    items.append("God's_Tear")

                    print("You have obtained the item....God's Tear")

                    #shows item in the list
                    print("Your items are now...", items)   

                elif userChoice == 'west':
                    print("Lets hope you chose all the right rooms...you're about to fight satan...")
                    print("goodluck...")
                    print("these are your current stats...")    
                    print("Player Name:",name,"\nCurrent Items In Inventory:", items,"\nCurrent Hitpoints:",hitpoints,"\nCurrent Location",location)
                    return items,hitpoints,location,name   
        else:
            print("You must have a final boss key or cerberus's head to continue")

#final bossfight room, fight against satan, scales off of items collected
def Satan(items, hitpoints, location, name):
    
    location = 'Satan'
    #makes sure the player actually has the key and not just the room name. Did not make this game easy because I am a psychopath who likes difficult games.
    if 'Final_Key' in items and location == 'Satan':
        print("You unlock the door to the final room....")
        print("Welcome", name)
    #these statements arrange the player base damage for this fight based on the items that have been collected.
        if 'Holy_Sigil' in items and 'Divine_Light' in items and 'Amulet_Of_Fury' in items and 'God_Slayer_Scythe' in items and 'Cerberus_Heads' in items and 'Satans_Bane' in items and 'Draconic_Claw' in items and "God's_Tear":
            playerAttack = 5000000
        elif 'Holy_Sigil' in items and 'Divine_Light' in items and 'Amulet_Of_Fury' in items and 'God_Slayer_Scythe' in items and 'Cerberus_Heads' in items and 'Satans_Bane' in items and 'Draconic_Claw' in items:
            playerAttack = 1000000
        elif 'Holy_Sigil' in items and 'Divine_Light' in items and 'Amulet_Of_Fury' in items and 'God_Slayer_Scythe' in items and 'Cerberus_Heads' in items and 'Satans_Bane' in items:
            playerAttack = 500000
        elif 'Holy_Sigil' in items and 'Divine_Light' in items and 'Amulet_Of_Fury' in items and 'God_Slayer_Scythe' in items:
            playerAttack = 20000
        else:
            #I made the game force quit, because I didn't want a death to be warranted, but I was going to make this satan smash you dead, because your buffs are that poo.
            print("You Do Not Have the correct items..")
            save_game(items,hitpoints,location,name)
            quit()
        
        #fight engages where player health is randomized, I could have no used random, but I re-used code from previous code, because I have spent alot of time on this final. heh.
        satanHealth = 10000000
        satanDamage = 100
        while satanHealth >= 0 and hitpoints >=0:
            playerAttack = random.randint(1999,playerAttack )
            satanHealth-=playerAttack
            print("You attack Satan for", playerAttack, "damage. Satan has", satanHealth, "health left.")
            time.sleep(0)

            satanDamage = random.randint(99,satanDamage)
            hitpoints -= satanDamage
            print("Satan Attacks you for", satanDamage, "damage. You have", hitpoints, "health left.")
            time.sleep(0)
                            
                            
            # Checks to see if the player is dead and saves the game if you actually die.
            if hitpoints <= 0:
                print("CERBERUS CRUSHES YOUR HEAD INTO THE BASE OF YOUR SPINE")
                print("YOU'RE DEAD")
                save_game(items,hitpoints,location,name)
                quit()
            #some weird thing happens here with health like in the previous, but I figured I'd leave it, because the npc would hit you once even if it was dead. Whatever though.
            #I plan to keep this on my github and fix it over the summer when I have time and analyze this a bit more.            
                        
            elif satanHealth <= 0:
                print("YOU HAVE BEATEN THE GAME")
                time.sleep(5)
                print("You now have escaped hell! Your sins have been cleansed!")
                time.sleep(5)
            #some weird thing happens here with health like in the previous, but I figured I'd leave it, because the npc would hit you once even if it was dead. Whatever though.
            #I plan to keep this on my github and fix it over the summer when I have time and analyze this a bit more. This is no exception..
                
                #cool ascii art because you win
                print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡠⠤⠀⠂⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡶⢠⠆⡰⡦⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠒⠤⠤⠤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠴⠢⠔⠒⠓⠆⡠⠤⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣔⣿⡃⠏⣠⣧⡸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠩⠕⣒⣈⡲⠤⡤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠡⢒⠞⡒⢉⠀⡀⠀⠀⠉⠓⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⡿⢯⠞⠀⠀⠡⠈⢽⣾⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠥⣞⢩⣙⠧⠄⢀⡠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⢲⠂⡴⢠⠜⢋⠄⣀⣀⣈⡱⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢻⡘⠘⠇⠀⠀⠀⡄⠘⢾⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢌⡒⠒⠂⠀⠒⠲⢹⣮⠁⠀⢀⡠⠖⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠄⠀⠀⠋⣱⡔⣁⠴⠁⢒⠀⢀⠀⠌⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⠀⡰⡰⠀⠀⠀⠁⠢⢨⣷⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⣉⡫⢥⢥⣀⣢⠥⠤⢤⣤⠗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⡂⠀⠀⠀⢸⠜⠪⠭⠯⠤⠀⡀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡅⢸⠀⠀⢀⠀⠀⠃⠔⣷⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠚⠩⠁⣀⠀⣱⣒⠒⠀⡤⠖⢋⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⢎⢠⠀⢓⠤⠐⠭⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣄⡆⠀⢀⣿⣆⠀⠀⣸⡽⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠤⠛⠒⠀⠀⣀⣐⡗⠊⣀⡀⠵⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣀⠀⠀⠀⠀⢋⣉⣇⣀⣐⣒⣂⠑⠒⠖⢦⡔⢂⡤⠒⠀⠀⠀⠀⠀⠀⠀⢻⣿⣷⡀⡾⣽⣿⡆⣸⣿⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠒⡶⣖⣛⠓⣀⣀⣀⣀⠀⠀⠘⠒⠀⣀⣠⡴⠂⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣲⣶⣤⣉⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣷⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣼⢟⣿⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠈⠉⠛⠉⠛⠛⠛⠛⠻⠿⢿⣿⣿⣿⣿⡽⢛⣾⣤⡄⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⢚⣽⣯⣼⣿⣿⡿⠿⠿⠻⠿⠟⠟⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠲⢦⣄⣀⠀⠐⢶⣶⣦⣬⣷⣾⣶⣦⣴⣤⡶⣤⣤⣤⣤⣄⠒⠄⡈⠿⠿⣾⣧⣦⠚⢿⣦⡀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⣠⠴⣟⣯⣳⣷⣿⠟⣋⠁⡀⠀⣀⣀⠀⢤⡠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢀⡀⠀⠀⠀⠙⢻⣿⣶⣶⣽⣿⣿⣿⣿⣿⣿⡿⠿⠛⠛⠓⠻⠿⣿⣿⣷⡢⠄⠀⠉⢹⣿⣷⣦⣯⣻⣦⣀⣠⠔⠀⠀⠀⢻⣿⣿⣿⡿⠀⠀⡀⠀⠀⠒⢀⡾⣁⣣⣷⣿⡿⠉⠀⠨⡀⠖⠤⡤⠀⠀⢀⡓⠭⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠹⣷⣦⣄⣀⠀⠈⠻⣿⣿⣿⣿⣿⠟⠋⠀⠀⣀⣤⣶⣾⣿⣿⣿⣿⡞⣭⣯⣽⠆⡄⠈⢿⣿⣿⣻⣿⣷⡄⠄⠀⠀⠀⢸⣿⣿⣿⡇⠀⠀⠀⠉⠀⡴⣧⣨⣿⣿⣟⠉⠀⠀⣉⡁⢄⠈⢭⣿⣾⣶⣦⣵⡂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠹⣿⣿⣿⣿⣷⣿⣿⣿⣿⡿⠁⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣮⣍⠻⠱⢭⣚⢮⣔⢀⠄⢹⣿⣿⣿⣿⣿⡄⠀⠀⠀⢰⣿⣿⣿⡇⠀⠀⠀⢀⣾⣭⣿⣿⣿⠋⠁⢀⠀⡀⠀⠀⠀⠀⠀⠈⠉⢿⣿⣿⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠹⣻⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⣴⣿⣿⣿⣿⣿⣯⣙⠻⠻⣿⣷⣤⡀⠀⠀⠈⠛⠈⠀⠹⣿⣿⣿⣯⣿⣆⠀⠀⢰⣿⣿⣿⣇⠀⠀⢀⣿⢞⣿⣿⣿⠋⠁⡀⠈⠊⠉⠒⠀⡀⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣷⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⡇⠀⠀⣸⣿⣿⣿⣵⡙⠋⠛⠛⠧⠀⠀⣨⣵⣿⡷⣦⡀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⡄⠀⣸⣿⣿⣿⣿⠀⢀⣾⣧⣿⣿⣿⠃⠀⠀⠈⠁⠀⢠⣞⢟⣿⣿⣦⡀⠀⠀⠀⠈⠻⣿⣻⣟⢿⣧⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠿⣿⣿⣿⣿⡆⠀⠀⣿⣿⣿⣿⣿⣷⣤⠀⠀⠀⠀⣰⣿⣿⣿⠋⠙⣧⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⡏⣹⣿⣷⣿⣿⣿⣿⣿⡃⠀⠀⠀⠀⠀⠂⡮⣿⢊⣿⣿⣽⣷⣄⠀⠀⠀⠀⠈⢷⣯⡣⢪⠈⠓⠆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠹⢿⣿⣿⣇⠀⠐⣿⣿⢿⣯⣿⢿⣿⣟⣄⡀⣰⣿⣿⣿⡧⣍⢩⣿⠀⠀⠀⠀⣠⣭⣿⣿⣿⡿⣿⣿⣟⠿⣹⣭⣹⣩⣿⣿⣿⣿⣿⡲⡒⠉⠁⠁⠀⠀⡇⡟⣽⣿⢿⣻⣿⣿⣷⢶⣦⣤⣀⣀⠙⡿⢷⣍⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠠⣄⡀⠀⠀⠀⠈⠿⣿⣿⣆⠀⣿⣿⣷⣍⠙⠻⣿⣻⣝⢶⣿⣿⣿⣿⣿⣒⢹⣿⣀⣤⣤⣾⣿⢿⡿⣿⣿⡿⡝⣻⢿⡟⢞⣽⡣⢿⣿⣿⣿⣿⣿⣷⣶⣤⣀⣀⠀⠀⣣⡯⣳⡿⣾⣼⣿⣿⣿⣆⠉⠿⣿⡿⣿⣾⣷⣜⠻⠦⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠉⣷⣶⣤⣀⠀⠙⡿⣿⣦⣹⣿⣷⡉⠓⠤⠀⠈⠑⣿⣿⣿⣿⣿⣿⣯⢯⣿⡙⠻⠿⡿⣿⣿⣿⣿⣿⣿⣶⡷⣽⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠋⣿⡪⣺⣿⣿⣿⣿⣿⣿⣿⡆⠀⠈⠙⣾⢹⠿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠺⣿⣿⣿⣶⣦⣽⣿⣿⣯⣿⣫⠄⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣻⣿⣧⠀⠀⠀⢴⣿⣿⣿⣿⣟⣿⡿⣶⣽⣿⣿⣏⣷⣿⣟⣿⣿⣿⡽⡆⠀⠁⠀⠀⠀⣧⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⡄⠀⠀⠀⠙⢮⣙⠿⣿⣶⣤⣀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣷⣿⣿⣷⣞⡷⡀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⡽⣿⡷⣦⡀⢯⢻⣿⣿⣿⣿⠿⢿⣿⣿⡿⠿⣿⣿⣾⣿⣿⣿⣿⡯⡁⠂⠀⠀⠀⣸⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠙⣦⣧⣛⠿⣿⡶⢄⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠋⢿⣿⣿⣿⣿⣿⢿⣽⣳⢡⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣿⠫⣻⠦⠈⡽⢹⣿⣿⣿⣿⣿⡿⠡⢀⣿⣿⣿⣿⣿⣿⢸⠇⠀⠀⠀⠀⢠⠃⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣧⠀⠀⠀⣐⣤⣸⣷⡩⢛⠘⠛⠱⠎⣦⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⢯⣾⢻⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⡀⠈⠫⢓⡃⢀⠻⣿⣿⣿⣗⣫⣅⣀⣿⣿⣿⡿⠏⠃⠊⠀⠀⠀⠀⢠⠯⢫⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠈⠪⡛⢿⣕⡳⡂⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠸⣾⡿⠀⡍⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣷⡀⠀⠀⠁⠀⠁⣹⣿⣿⣿⣯⡛⠛⣿⣿⣿⣷⣀⠀⠀⠀⠀⠀⢀⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⡄⠂⡈⠳⢮⣄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣳⡅⠀⢈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⣠⣴⠾⠃⢻⣿⣷⣽⣃⣘⣿⣿⣿⠙⠛⠻⣶⣄⣀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠈⢄⠈⠠⡀⠈⠓⢦⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⡼⡀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠛⢂⠁⠀⠀⢰⣿⣿⣭⡉⣩⣿⣿⣯⠀⠀⠀⠘⠉⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠑⢄⠀⠀⠀⠀⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣹⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠁⠀⠀⠸⣾⢿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠂⠑⢄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣏⠂⣠⡄⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⡀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠑⢄⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣄⠉⠔⡄⠹⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⢀⡄⠀⠀⠀⠀⠀⠈⣱⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠈⢾⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣷⠑⠈⡔⢂⠻⣿⣿⣿⠟⠁⠀⠀⠀⠀⢀⣴⣿⠀⠀⣠⡀⠀⠀⠀⡆⣷⣛⣧⡿⡏⠀⠀⠀⢀⣀⠀⣿⣿⠿⠿⣿⡿⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣧⠀⠀⠮⠀⡛⠟⡡⠂⠀⠀⢀⡴⣶⣿⣿⣿⢆⠠⣉⠁⠀⢀⣀⣸⢻⠸⡺⡇⠁⠀⠀⠀⣈⣻⣿⣿⣿⣔⡶⣶⣺⢹⣼⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣧⣀⡀⠫⠩⠀⠀⠀⢀⣼⣟⣿⣿⣿⣿⣿⣞⠳⡦⣭⣵⣽⣿⠓⢻⡱⣿⡰⠁⣷⣤⣌⣿⣿⣿⣿⣿⣿⣦⣁⠧⢳⢻⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣕⢄⣀⣀⢠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⡶⢣⠙⠿⡟⢟⢤⣊⣧⡏⣧⣴⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⡀⠈⣸⣇⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣽⣻⣞⣽⢫⣞⡻⠼⣿⠯⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠉⡤⢤⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣿⣿⣿⣿⣃⣀⣾⣿⡭⡕⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠄⠀⡤⡄⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠷⣿⠉⠠⢄⣹⣿⡏⠀⠀⢹⢮⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣎⠀⠀⠲⡢⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠿⣿⣿⣿⣿⣿⣿⡿⢋⣤⢾⣿⣶⣿⣿⣿⡏⣿⣿⣶⢾⣏⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⢶⣄⠑⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠁⠀⠈⢿⡿⣿⣿⣿⠟⢡⢻⣷⣿⣿⣿⣿⣿⣿⢂⡿⢟⣵⣿⣿⣿⣮⡁⠀⢻⣿⣿⣿⣿⣿⣿⣿⡟⢿⠀⠈⠳⣦⣄⢁⡹⢿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣹⣽⠃⠀⠀⠀⠀⠀⠀⠙⢣⠏⠠⢃⣿⣿⣿⣿⣿⣿⣿⣿⣯⣴⣟⢿⣿⣿⣿⣿⣿⡄⡀⢻⣿⣟⣻⣿⡏⠛⠃⠀⠀⠀⠀⠘⢿⠤⠁⠀⠀⠉⢙⠻⢿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⡟⠉⠀⠀⠀⠀⢀⡔⢊⠭⠙⠛⠢⠤⢾⣿⣿⣿⣿⣿⢣⣾⣿⠟⣿⣿⡇⢿⣿⣿⣿⡿⠟⠊⠉⠀⢉⣮⣭⣍⣓⣦⣄⡀⠀⠀⠀⠘⣄⠀⠐⢨⡙⣻⣿⣿⣾⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⢟⠏⠀⠀⠀⠀⠀⠠⡯⣽⡵⢦⣶⣶⣀⠀⣄⡀⠙⠻⣿⣇⢸⣿⣿⠀⣿⣿⡟⣸⣿⠟⣉⣠⣴⣾⠇⠀⠀⠿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠈⢢⢀⢻⢸⣠⢿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣽⡿⣹⣿⡿⠃⠀⠀⠀⠀⠀⠀⣠⠶⠋⠁⠀⣀⣀⠈⠙⠓⠜⣿⣄⠀⠈⠻⣮⡻⣇⠀⢾⣿⡵⢛⣵⣾⣿⡿⠿⣋⠴⠇⠀⠀⠈⠻⢿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠛⠘⠚⡌⢎⢻⣿⣿⣿⣿⡿⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣫⣿⡷⠙⠉⠀⠀⠀⠀⠀⠀⡠⠊⠁⠀⠀⠀⠀⠀⠈⠛⢶⣤⡀⠀⠛⢧⣲⣦⣀⡛⠚⠓⢛⣫⣶⣿⠿⢋⣡⠄⠀⠈⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠈⠢⣳⣿⣿⣿⣿⣯⢷⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⡿⠓⠁⠀⠀⠀⠀⠀⠀⠰⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣷⣦⡄⠀⠛⢿⣿⣿⣿⣿⣿⣿⢟⣷⠆⠉⠀⢀⡠⠴⠒⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠈⠿⣿⣿⣿⣿⣟⡆⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⡜⠀⠀⢀⡀⠀⠀⠀⠤⡀⠄⡀⠀⠀⠈⠿⣿⣷⡀⣀⡉⠙⣛⣿⣿⡇⣾⡏⡀⡠⠞⠁⣀⣤⣤⣶⣶⣶⣦⡀⠀⠀⠀⠛⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣶⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⣄⢰⢄⡙⢂⠀⠀⠀⠀⠘⠠⠄⠀⠀⠀⠙⡿⣿⣾⣿⣿⣿⣿⣿⣧⠘⣡⣤⣶⡾⠟⠋⠡⢶⣶⣍⣉⠉⠁⠀⠀⠀⠀⢻⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⡆⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣿⣿⠏⠘⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣷⣟⠦⣌⠁⠀⠀⠀⠀⠀⠀⠀⠸⣄⠘⡿⢿⠻⠿⣿⣿⣿⣿⣷⠿⠋⢡⣤⣦⣔⣦⣶⣠⣤⠌⠉⠁⠀⠀⠀⠀⢸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠸⣿⣷⠀⠀⠀
⠀⠀⠀⠀⠀⠸⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣮⣝⠲⢤⠀⠀⠀⠠⠄⠀⠀⢁⡈⠀⢠⣼⣿⣿⣿⠟⣁⣠⣶⣷⣿⣿⣿⣿⣿⣿⣶⣦⡤⠀⢀⠀⡀⣀⣼⣿⡿⠀⠀⠀⠀⠀⠀⠀⠙⢶⣄⡀⠀⠀⠀⠀⠹⣿⡆⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣷⣿⣶⣧⣄⡀⠀⢀⣤⣤⣍⣤⣀⣽⣿⣿⣿⣷⣶⣌⣯⣽⣿⣿⣿⣿⣿⣿⣿⣿⣵⣾⣶⣾⣽⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣦⠀⠀⠀⠀⠘⠿⠀⠀
⠀⠀⠀⠀⠀⠀⣀⡤⠤⠀⠀⠀⠠⢤⣤⣤⣤⣤⣶⣀⣀⣀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣯⣿⣹⣭⣿⣿⣿⣿⡿⢛⣭⣤⣶⣶⣶⣀⣀⣈⣉⠉⠙⢛⡛⠛⡟⠿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣷⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⢮⠭⡭⠭⠥⠥⠤⠶⠶⣶⣿⣿⣿⣷⡭⢤⣀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣽⣿⣿⣿⣿⣿⡯⣿⡿⣿⣭⣶⣿⣿⣾⣿⣿⣿⣿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠉⠭⠷⣯⢭⣭⣭⣥⣬⣬⣭⣭⣽⣶⣶⣶⡄⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⣿⠿⢧⠒⣍⣇⢿⡹⡻⣟⣟⣿⣿⣟⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠛⠛⣿⣽⣭⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣳⣶⣦⣤⡤⠄⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣮⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣐⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣛⣛⣟⣻⣯⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣻⣹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣀⣙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣏⣛⡂⠀⢸⡶⡿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⢶⣓⣻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣾⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠩⢭⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⡦⠄⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣿⣿⡿⢿⣿⠀⠀⠀⠀⠙⠳⣶⣶⣶⣾⣿⣿⣿⣿⡿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⡄⠐⢄⣨⠉⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠖⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣹⣿⣿⣿⣷⣾⣿⠀⠀⠀⠀⠀⠀⠉⠙⠛⠛⠟⠛⠛⠉⠁⠀⠀⡀⠐⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠳⠼⣆⠈⢃⣠⣄⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠋⢉⣡⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣀⠀⠀⠀⠀⠀⠀⣀⣀⣲⣤⣤⡠⠤⠤⡤⠮⠄⠐⠢⠤⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⢆⡾⢱⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠉⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⠯⠅⠓⠒⠓⢢⠖⣣⢞⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣯⢿⣿⣿⣿⣷⣤⣀⣤⣤⣯⣬⣭⣿⣿⣿⣾⣯⣿⣿⣿⣲⣘⡒⣤⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣭⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⢿⠃⣠⣾⣿⣿⣿⣿⣿⠭⠛⠛⢿⠇⠀⠀⠀⠀⠀⠀⠉⠀⡉⠭⣙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⠿⠓⠰⠔⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⡩⠽⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣟⢲⣖⠒⢤⠄⢠⠀⢠⢤⠀⡄⢀⡀⠐⡑⢉⣋⡙⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣧⣤⣖⡤⠤⠒⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠭⣵⠾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣭⡙⠯⠀⠮⠤⠎⡀⠯⠁⠸⠁⠼⠀⠜⢇⣨⣷⣛⣻⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡷⡶⠯⠏⠉⠑⣢⠤⠆⠀⠀
⠀⠀⠀⠀⠐⠒⠚⠙⢉⣯⣭⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡾⣵⣲⠯⠁⡆⡠⠃⡴⠀⠀⢠⠞⣆⠴⠒⡰⠀⠚⣭⣛⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⠷⠒⠢⠬⣉⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠴⠶⠾⠾⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣽⡿⣽⣽⢾⡿⢧⠭⠤⠤⠭⠤⠤⠭⠩⠈⠉⠁⠓⠂⠉⠻⠟⠻⠛⠿⠿⠿⠿⠿⠿⠿⠿⢿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣟⣛⠉⠭⠽⠭⢭⣥⠤⡤⠀⠀⠀⠀""")
                return items, hitpoints, location, name
            
def main():

    #calls loading screen
    loading_screen()

    #calls the title screen (loading....)
    title_screen()
    


    #inializes all items inside main
    
    items = []
    hitpoints = 100
    location = ''
    name = ''

    #while loop initilization
    menu_selection = ''


    while menu_selection != '0':
        print("""
                ███████████████████████████
                ███████▀▀▀░░░░░░░▀▀▀███████
                ████▀░░░░░░░░░░░░░░░░░▀████
                ███│░░░░░░░░░░░░░░░░░░░│███
                ██▌│░░░░░░░░░░░░░░░░░░░│▐██
                ██░└┐░░░░░░░░░░░░░░░░░┌┘░██
                ██░░└┐░░░░░░░░░░░░░░░┌┘░░██
                ██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
                ██▌░│██████▌░░░▐██████│░▐██
                ███░│▐███▀▀░░▄░░▀▀███▌│░███
                ██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
                ██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
                ████▄─┘██▌░░░░░░░▐██└─▄████
                █████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
                ████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
                █████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████
                ███████▄░░░░░░░░░░░▄███████
                ██████████▄▄▄▄▄▄▄██████████
                ███████████████████████████
              """)
        
        print('                         1.Save Game\n                         2.Load Game\n                         3.Start Game\n                         4.Tutorial\n                         0.Exit Game')
        menu_selection = input("ᶜᴴᴼᴼᔆᴱ ᵂᴵᔆᴱᴸᴱʸ>>>>:")
        
        if menu_selection == '1':
            save_game(items,hitpoints,location,name)
        
        elif menu_selection == '2':

            items,hitpoints,location,name = load_game(items,hitpoints,location,name)
        
        #game start from scratch or load state optional, checks for proper location in data folder to initiate correct room sequence.
        elif menu_selection == '3':
            #checks for load location variable to corresponding room
            if location == '':
                items,hitpoints,location,name = roomOne(items,hitpoints,location,name)
            
                items, hitpoints, location, name = questionOne(items, hitpoints, location, name)

                items, hitpoints, location, name = roomTwo(items, hitpoints, location, name)

                items, hitpoints, location, name = roomThree(items, hitpoints, location, name)

                items, hitpoints, location, name = roomFour(items, hitpoints, location, name)
            
                items, hitpoints, location, name= roomFive(items, hitpoints, location, name)

                items,hitpoints,location,name = Satan(items,hitpoints,location,name)
            #checks for load location variable to corresponding room
            elif location == 'questionOne' and 'Holy_Sigil' in items:
                items, hitpoints, location, name = questionOne(items, hitpoints, location, name)

                items, hitpoints, location, name = roomTwo(items, hitpoints, location, name)

                items, hitpoints, location, name = roomThree(items, hitpoints, location, name)

                items, hitpoints, location, name = roomFour(items, hitpoints, location, name)
            
                items, hitpoints, location, name= roomFive(items, hitpoints, location, name)

                items,hitpoints,location,name = Satan(items,hitpoints,location,name)
            #checks for load location variable to corresponding room
            elif location == 'roomTwo':
                items, hitpoints, location, name = roomTwo(items, hitpoints, location, name)

                items, hitpoints, location, name = roomThree(items, hitpoints, location, name)

                items, hitpoints, location, name = roomFour(items, hitpoints, location, name)
            
                items, hitpoints, location, name= roomFive(items, hitpoints, location, name)

                items,hitpoints,location,name = Satan(items,hitpoints,location,name)
            #checks for load location variable to corresponding room
            elif location == 'Gluttony':
                items, hitpoints, location, name = roomThree(items, hitpoints, location, name)

                items, hitpoints, location, name = roomFour(items, hitpoints, location, name)
            
                items, hitpoints, location, name= roomFive(items, hitpoints, location, name)

                items,hitpoints,location,name = Satan(items,hitpoints,location,name)
            #checks for load location variable to corresponding room
            elif location == 'avarice':
                items, hitpoints, location, name = roomFour(items, hitpoints, location, name)
            
                items, hitpoints, location, name= roomFive(items, hitpoints, location, name)

                items,hitpoints,location,name = Satan(items,hitpoints,location,name)
            #checks for load location variable to corresponding room
            elif location == 'roomFive':
                items, hitpoints, location, name= roomFive(items, hitpoints, location, name)

                items,hitpoints,location,name = Satan(items,hitpoints,location,name)
            #checks for load location variable to corresponding room
            elif location == 'Satan':
                items,hitpoints,location,name = Satan(items,hitpoints,location,name)

        elif menu_selection == '4':
            tutorial()
        #game quit
        elif menu_selection == '0':
            quit()
        #handles incorrect input
        else:
            print("Invalid Input...")



#calls the main function
main()





#################################################################################################################################
#                                                    Cheat Code                                                                 #
#  Enter Any Name, next type north, limbo, east, west, east, west, west, south, virgil, 7(or)seven , north, south, east, west   #
#################################################################################################################################