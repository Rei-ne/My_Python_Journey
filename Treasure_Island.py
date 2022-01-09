print('''
 _________   
|:::   :::| 
|:::   :::| 
|:::___:::| 
           
                  * | *
                 * \|/ *
            * * * \|O|/ * * *
             \o\o\o|O|o/o/o/
             (<><><>O<><><>)      
             '====REINE===='  	     
''')
print("Welcome to Treasure Island.(Lagos Version)")
print("Your mission is to find the treasure.")


def treasure_island():
    continue_to_play = True
    while continue_to_play:
        # print("Welcome to Treasure Island.(Lagos Version)")
        # print("Your mission is to find the treasure.")
        choice1 = input(
            'You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
        if choice1 == "left":
            choice2 = input(
                'You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
            if choice2 == "wait":
                choice3 = input(
                    "You arrive at Lagos island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
                if choice3 == "red":
                    print('It\'s a room full of street touts. They ask "anything for the boys"\nYou don\'t have anything for them so they take all your belongings and leave you stranded.\nGame Over.')
                elif choice3 == "blue":
                    print("You found the treasure! You Win!")
                elif choice3 == "yellow":
                    print(
                        "You enter a room of beautiful women.\nYou got distracted and then lost track of the mission.\nGame Over.")
                else:
                    print("You chose a door that doesn't exist. Game Over.")
            else:
                print(
                    "You try to swim in the murky water. Your leg gets caught in some sea debris and you drown.\nGame Over.")
        else:
            print(
                "You did not see the okada man coming. He hits you off the road.\nGame Over.")

        to_play = input(
            "Do you want to continue playing? Type 'y' for yes or 'n' for no: ").lower()
        if to_play == 'y':
            treasure_island()
        else:
            continue_to_play = False
            print("{:s}".format("Thank you for playing"))


treasure_island()
