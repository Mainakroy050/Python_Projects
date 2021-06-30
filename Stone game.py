import random
lst=['s','p','x']

chance = 5
no_of_chance=0
computer_point=0
user_point=0

print("\t\t\t\t STONE , PAPER , SCISSOR\t\n\n")
print("\'s\' -for STONE\t \'p\' -for PAPER\t \'x\' -for SCISSOR\t :")

while no_of_chance < chance:
    _input = input('STONE , PAPER , SCISSOR : ')
    _random = random.choice(lst)

    if _input == _random:
        print("Tie Both 0 point to each\n")
        print(f"you hv entered {_input} and computer also chooses {_random}")
    ###### for STONE I/P ###############

    elif _input=="s" and _random == "x":
        user_point=user_point+1
        print(f"You have entered {_input} and computer entered {_random}\n")
        print("User wins 1 point\n")
        print(f"You have {user_point} point and computer has {computer_point} point\n")


    elif _input=="s" and _random == "p":
        computer_point=computer_point+1
        print(f"You have entered {_input} and computer entered {_random}\n")
        print("Computer wins 1 point\n")
        print(f"You have {user_point} point and computer has {computer_point} point\n")

    ################# for PAPER I/P ##############

    elif _input=="p" and _random == "s":
        user_point=user_point+1
        print(f"You have entered {_input} and computer entered {_random}\n")
        print("You won 1 point\n")
        print(f"You have {user_point} point and computer has {computer_point} point\n")


    elif _input=="p" and _random == "x":
        computer_point=computer_point+1
        print(f"You have entered {_input} and computer entered {_random}\n")
        print("Computer gets 1 point\n")
        print(f"You have {user_point} point and computer has {computer_point} point\n")

    ###################### for SCISSOR I/P ################


    elif _input=="x" and _random == "p":
        user_point=user_point+1
        print(f"You have entered {_input} and computer entered {_random}\n")
        print("You won 1 point\n")
        print(f"You have {user_point} point and computer has {computer_point} point\n")


    elif _input=="x" and _random == "s":
        computer_point=computer_point+1
        print(f"You have entered {_input} and computer entered {_random}\n")
        print("Computer wins 1 point\n")
        print(f"You have {user_point} point and computer has {computer_point} point\n")

    else:
        print("\t\t\t\tYou have entered a wrong input !!!!!!! \n")


    no_of_chance=no_of_chance+1
    print(f"{chance-no_of_chance} no of chances is left out of {chance} chances \n")

print("GAME OVER !!!!")

if computer_point== user_point:
    print("Tie!")
elif computer_point > user_point:
        print("Computer wins and You lose")
else:
    print("Congratulations you won the game !")

print(f"Your point is {user_point} and computer point is {computer_point}\t")


