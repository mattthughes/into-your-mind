
def welcome_message():
    """
    This function will greet the user and allow them to 
    enter there first name
    """

    print("Welcome to your nightmare, the journey to madness has begun but how crazy can it truly get?")

    while True:
        username = input("What is your name?\n")

        if not username:
            print("Please enter your name.\n")
        else:
            intro(username)
            break

def abandoned_bus(username):
    print("Abandoned bus")

def open_door(username):
    """ 
    This function id the third section of the game
    allowing the user to pick one out of three options
    """
    print("\nAs you explore the abandoned school you notice an open door and an open window.")
    print("Do you A go through the door. B slam the door shut or C go through the open window and escape.\n")

    while True:
        try:
            open_door_choice = input("Please type either A or B or C\n").upper()
            if open_door_choice == "A":
                print("You went through the open door, and were attacked and then eaten by an alien, one of your")
                print("biggest fears you die.\n")
                welcome_message()
                break
            elif open_door_choice == "B":
                print("You slammed the door shut and alerted the principal, he")
                print("finds you and takes you to his office. The principal begins to laugh at you")
                print("you get up and try and escape but the door is locked the principal begins to laugh")
                print(f"even more and starts to repeat you are here forever {username} HAHAHAHAHAHA!\n")
                print("Please try again.\n")
                welcome_message()
                break
            elif open_door_choice == "C":
                print("You went through the open window leading you to the outside playground.")
                print("escaping the monster through the open door.\n")
                print(f"You escaped for now {username}\n")
                abandoned_bus(username)
                break
            else:
                print("Please pick a valid format by either typing A or B or C.\n")
                continue
        except ValueError as e:
            print(f"{e} please fill in the right format\n")



def escaped_classroom(username):
    """
    This function is the second section of the game, this allows the user 
    to pick one out of three options
    """

    print("As you escape the classroom you notice a small dog in the corridor.")
    print("Do you A throw your book at the dog. B turn around or C pet the dog.")

    while True:
        try:
            escaped_choice = input("Please type either A or B or C.\n").upper()
            if escaped_choice == "A":
                print("You throw a science book at the dog causing an explosion")
                print("killing the dog, well done you live to fight another day.")
                open_door(username)
                break
            elif escaped_choice == "B":
                print("You turn around and you spot an even bigger dog, before you can react")
                print("the dog bites you try to escape but you feel yourself slowing losing control,")
                print("you faint and as you lay there you can feel yourself getting weaker. As you slowly lose your ")
                print("soul to the underworld.")
                print("Please try again.")
                welcome_message()
                break
            elif escaped_choice == "C":
                print("\nYou pet the dog and the dog turns around and bites you,")
                print("you have been lost to the underworld forever.\n")
                print("Please try again.\n")
                welcome_message()
                break
            else:
                print(f"Please use the correct format by typing either A or B or C. {username}")
                continue
        except ValueError as e:
            print("Invalid format please try again.")


def run_game(username):
    """
    This is the first section of the game this function will allow the user 
    to read a senario and make a decision
    """

    print("\nYou wake up in detention and you hear the principal in the background storming to your class room.")
    print("You have three choices do you A go back to sleep and pretend its all just a bad dream. B wait for the principal to arrive")
    print("or C do you hide in the cupboard away from the principal?")

    while True:
        try:
            first_choice = input(f"\nPlease type either A or B or C pick carefully {username}\n").upper()
            if first_choice == "A":
                print("\nYou go back to sleep and the principal rushes in and throws a slice of pizza at your head. which is")
                print("a massive fear of yours, you faint and die please try again\n")
                welcome_message()
                break
            elif first_choice == "B":
                print("\nYou hide in the cupboard and watch the principal storm into the classroom after searching the classroom he")
                print(f"shortly leaves after. You have escaped for now {username}\n")
                escaped_classroom(username)
                break
            elif first_choice == "C":
                print("\nYou wait for the principal who has backup one of your biggest fears a maths test.")
                print("You do your best but you fail the maths test, the principal laughs sniggering at you")
                print("repeating you will remain here forever HAHAHAHAHA!\n")
                print("Please try again.\n")
                welcome_message()
                break
            else:
                print("Please enter the correct format either A or B or C\n")
                continue
        except ValueError as e:
            print(f"Invalid format please enter the correct format user {username}")
                

def view_instructions(username):
    """
    This function will display the instructions to the user
    teaching them how the game works and any key information
    they will need while playing the game
    """

    print("\nInstructions")
    print("\nInto Your Mind is a text based action adventure game where your decisions really matter.")
    print("During the game you will recieve a situation where your answer matters, you will select your options by either typing A or B or C.")
    print("Depending on the situation you find yourself in think carefully as the wrong answer could mean Game Over.")
    print("If you would like to leave the game early at any point you can type EXIT to leave the application\n")

    while True:
        try:
            start = input("Please type either A to start the game or B to return to the main menu\n").upper()
            if start == "A":
                run_game(username)
                break
            elif start == "B":
                intro(username)
                break
            else:
                print("\nPlease enter the correct format by either typing A or B")
        except ValueError as e:
            print("Invalid format please use the correct format")
            

def intro(username):
    """
    This function will intro the user to the game 
    allowing them to view the instructions or start the game
    """

    print(f"\nWelcome to Into Your Mind {username} if you would like to Start the game type A or if you would like to view the instructions type B")

    while True:
        try:
            intro_msg = input("Please type either A or B\n").upper()
            if intro_msg == "A":
                run_game(username)
                break
            elif intro_msg == "B":
                view_instructions(username)
                break
            else:
                print("Please enter a valid format\n")
        except ValueError as e:
            print(f"\n {e} please pick the correct one")

welcome_message()