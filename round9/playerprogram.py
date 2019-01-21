# CS-A111 Fall 2018
# A test program for Exercise 9.3
# Author Kerttu Pollari-Malmi
#
# The main program has not been split to several functions to keep 
# it as simple as possible for beginners.

import player

# A function to read an integer with exception handling.

def read_integer():
    int_ok = False
    while not int_ok:
        try:
            luku = int(input())
            int_ok = True
            return luku
        except ValueError:
            print("Invalid integer. Enter a new intetger!")

def main():
    name1 = input("Enter the name of the first player.\n")
    name2 = input("Enter the name of the second player.\n")
    player1 = player.Player(name1)
    player2 = player.Player(name2)

    print("First player:")
    print("Name:", player1.get_name())
    print("Number of games:", player1.get_no_of_games())
    print("Record:", player1.get_record())
    print("Average: {:.2f}".format(player1.average()))
    if player1.is_master():
        print("The player has a master title.")
    else:
        print("The player has not achieved a master title.")
    print()
    print("Second player:")
    print("Name:", player2.get_name())
    print("Number of games:", player2.get_no_of_games())
    print("Record:", player2.get_record())
    print("Average: {:.2f}".format(player2.average()))
    if player2.is_master():
        print("The player has a master title.")
    else:
        print("The player has not achieved a master title.")
    print()
    
    print("Adding game results...")
    print("How many games will be added to the first player?")
    count1 = read_integer()
    for i in range(count1):
        print("Enter the points of the next game.")
        gamepoints = read_integer()        
        player1.add_game(gamepoints)
    print("How many games will be added to the second player?")
    count2 = read_integer()
    for i in range(count2):
        print("Enter the points of the next game.")
        gamepoints = read_integer()        
        player2.add_game(gamepoints)
        
    print("The playes after adding the games:")
    print("Name:", player1.get_name())
    print("Number of games:", player1.get_no_of_games())
    print("Record:", player1.get_record())
    print("Average: {:.2f}".format(player1.average()))
    if player1.is_master():
        print("The player has a master title.")
    else:
        print("The player has not achieved a master title.")
    print("Name:", player2.get_name())
    print("Number of games:", player2.get_no_of_games())
    print("Record:", player2.get_record())
    print("Average: {:.2f}".format(player2.average()))
    if player2.is_master():
        print("The player has a master title.")
    else:
        print("The player has not achieved a master title.")
    print()
    
    if player1.is_better(player2):
        print("The first player is better than the second player.")
    elif player2.is_better(player1):
        print("The second player is better than the first player.")
    else:
        print("The players are equal.")
    print
    
    print("The player information by using method __str__:")
    print(player1)
    print(player2)
    
    
main()