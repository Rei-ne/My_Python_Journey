from random import choice

list1 = ['Sit on a couch', 'Do a handstand', 'Jump up and down', 'Demonstrate yoga', 'Act like Darth Vader is choking you',
         'Do 5 pushups', 'Lay down', 'Put on a hat', 'Drink a cup of water', 'Touch the wall']
list2 = ['while picking you nose', 'while holding you nose', 'while singing', 'while tapping your head', 'while pregnant',
         'while singing jinglebells', 'while drinking water', 'while laughing', 'while clapping your hands', 'while stomping your feet']
list3 = ['your mom', 'your best freind', 'the wall',
         'a cat', 'a keyboard', 'your neighbor', 'a phone']


def my_game():
    continue_to_play = True
    while continue_to_play:
        count = int(input("How many dares would you like: "))
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
            print("{:s}".format("Thank you for playing"))
            continue_to_play = False


my_game()
