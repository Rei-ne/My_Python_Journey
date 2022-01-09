from random import choice

list1 = ['Sit on a couch', 'Jump up and down', 'Demonstrate yoga', 'Act like Buhari',
         'Do 5 pushups', 'Lay down', 'Take 3 shots', 'Drink a bottle of water', 'Dance to any song']
list2 = ['while picking your nose', 'while scrolling on your phone', 'while singing', 'while tapping your head', 'while pregnant',
         'while singing jinglebells', 'while shaking your butt', 'while laughing', 'while clapping your hands', 'while stomping your feet']
list3 = ['your mom', 'your best friend',
         'the wall', 'the mirror', 'everyone', ]


def my_game():
    continue_to_play = True
    while continue_to_play:
        print("Welcome to Reine\'s Python Snakebite Dare game!")
        print("These are the rules of the game:\nYou can pick from a number of 1-10 dares at a time")
        count = int(input("How many dares would you like?: "))
        if count < 1 or count > 10:
            print("Maximum of 10 dares and minimum of 1 dare allowed!")
        elif count <= 10:
            for num in range(count):
                print(
                    f"Dare: {choice(list1)} {choice(list2)} infront of {choice(list3)}")

        to_play = input(
            "Do you want to continue playing? Type 'y' for yes or 'n' for no: ").lower()
        if to_play == 'y':
            my_game()
        else:
            continue_to_play = False
            print("{:s}".format("Thank you for playing"))


my_game()
