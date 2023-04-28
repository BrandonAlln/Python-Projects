#Create a taste journal that temporarily stores different foods and their assessment of flavors
#----------------------------------------------------------------------------------------------
#1. Users should be able to add a new food : and their flavor reviews
#2. Users should be able to look up an existing food to see what they thought of them previously
#3. Program should handle incorrect input.
#4. Needs update capability
#-----------------------------------------------------------------------------------------------


#1#
def add_entry(food_dictionary):
    exit = ''
    while exit != '0':
        food_name=input('What is the food being entered called?  :')
        description=input('What is the description of that food? : ')
        food_dictionary[food_name]=description
        print(food_dictionary)
        exit = input("Press Any Key To Continue or Hit 0 To Exit: ")


#6#
def print_dictionary(food_dictionary): 
    for key, value in food_dictionary.items():
        print(key, "\t :", value)


#2#
def search_by_key(food_dictionary):
    exit = ''
    while exit != '0':
        print("Enter the name of the food to see its description")
        key=input('>>>>:')
        value=food_dictionary.get(key, "That Food Name Was Not found, Try Another! (The Key is case sensitive)")
        print(key, "\t :", value)
        exit = input("Press Any Key To Continue or Press 0 To Exit: ")




#4#
def remove_from_list(food_dictionary):
    exit=''
    while exit != '0':
        print("Would you like to remove a food from the list?")
        choice_remove = input("Y for Yes, N for No: ")
        if choice_remove == 'Y':

            
            food_remove = input("Enter A Food To Remove: ")
            
            if food_remove in food_dictionary:
            
                del food_dictionary[food_remove]
            
                print(food_dictionary)
            
            elif food_remove not in food_dictionary:
            
                print("______________________________")
                print("Error, Food Is Not In List..")

            
                exit=input("Exit? Hit 0 or Hit Another Key To Continue: ")
        
        elif choice_remove == 'N':
        
                print("Avoiding Removal...")
                exit=input("Press 0 To exit or any key to go back through: ")
        
        else:
            print("Invalid Input")
            exit=input("Enter 0 to Exit or any key to keep going: ")

    

#5#
def nuke_dictionary(food_dictionary):
    print("Are you sure you want to nuke this entire list?")
    print("Why would you even use this program dumdum?")
    choice_nuke = input("NUKE? Y = Yes, N = No!: ")
    if choice_nuke == "Y":
        print("I'm Flashing!")
        food_dictionary.clear()
        print(food_dictionary)
    elif choice_nuke == "N":
        print("Exiting For Your Saftey, Thermonuclear Warhead Avoided...")
        breakpoint
    else:
        print("Invalid Input!")


#3#
def update_description(food_dictionary):
    exit = ''
    while exit != '0':
        print("Enter The Name of A Food That You Would Like To Update The Description of!")
        updater=input("Food Name: ")
        exit = ''
        if updater in food_dictionary:
            newDescription = input("Enter A New Description: ")
            food_dictionary[updater]=newDescription
            print("Are You Finished? Press 0 To finish or any key to continue..")
            exit=input(">>>: ")
        if updater not in food_dictionary:
            print("Sorry This Food Was Not Found")
            exit = '0'
            
        
    


def main():
    food_dictionary = {}
    option = ''
    while option != '7':
         print("")
         print("----------------------------")
         print("Hi! And Welcome to my Guide!")
         print("Welcome to the food Journal!")
         print("----------------------------")
         print("----(1. Add A New Entry)-----")
         print("----(2. Search by Name )-----")
         print("--(3. Update A Description)--")
         print("---(4. Remove An element)----")
         print("----(5.NUKE ALL ENTRIES)-----")
         print("--(6. Show Full Dictionary)--")
         print("------(7. Exit Program)------")
         option = input("---Enter Menu Choice by #---: ")
         if option == '1':
            add_entry(food_dictionary)
         elif option == '2':
            search_by_key(food_dictionary)
         elif option == '3':
            update_description(food_dictionary)
         elif option == '4':
            remove_from_list(food_dictionary)
         elif option == '5':
            nuke_dictionary(food_dictionary)
         elif option == '6':
            print_dictionary(food_dictionary)
         elif option == '7':
            print("Exiting Program...")

         else:
            print("|----------------------------------------------------|")
            print("|Invalid Choice, Please Choose A Number On The Menu! |")
            print("|----------------------------------------------------|")


main()