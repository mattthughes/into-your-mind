import time

def output_delay(text_msg):
    for i in text_msg:
        print(i, end="", flush=True)
        time.sleep(0.07)

def loading_elements(loading):
    for i in loading:
        print(i, end="", flush=True)
        time.sleep(0.1)

def welcome_message():
    """
    This function will greet the user and allow them to 
    enter there first name
    """

    output_delay("\nWelcome to your nightmare, the journey to madness has begun but how crazy can it truly get?\n")

    while True:
        username = input("What is your name?\n")

        if not username:
            print("Please enter your name.\n")
        else:
            intro(username)
            break

def journey_home(username):
    print("Journey home")

def abandoned_bus(username):
    """ 
    This function will inform the user of the next senario giving them 
    two options to pick from 
    """
    text_msg = """
    You find an open school bus leading you out of the school.
    Do you A go through the school bus and head out the open 
    door or B hide under the bus seats.
    """
    output_delay(text_msg)

    while True:
        try:
            bus_choice = input("\nPlease type either A or B\n").upper()
            if bus_choice == "A":
                output_delay("\nYou go through the open bus and spot an exit, you quickly make a dash for the exit and escape the school.\n")
                output_delay("Now to find the way home and fast.\n")
                journey_home(username)
                break
            elif bus_choice == "B":
                output_delay("\nYou went through the open bus and hid under the seats, suddenly all the chewing gum under\n")
                output_delay("the seats has grown to the size of the school bus. Before you can react the chewing gum monster smothers you,\n")
                output_delay("takes your soul banishing you to the underworld forever.\n")
                welcome_message()
                break
            else:
                print(f"invalid format {username} Please type either A or B")
                continue
        except ValueError as e:
            print("Invalid format please type either A or B")

def open_door(username):
    """ 
    This function id the third section of the game
    allowing the user to pick one out of three options
    """
    text_msg = """
    As you explore the abandoned school you notice an open door and an open window.
    Do you A go through the door. B slam the door shut or C go through the open window and escape.
    """

    output_delay(text_msg)

    while True:
        try:
            open_door_choice = input("\nPlease type either A or B or C\n").upper()
            if open_door_choice == "A":
                output_delay("\nYou went through the open door, and were attacked and then eaten by an alien, one of your\n")
                output_delay("biggest fears you die.\n")
                welcome_message()
                break
            elif open_door_choice == "B":
                output_delay("\nYou slammed the door shut and alerted the principal, he\n")
                output_delay("finds you and takes you to his office. The principal begins to laugh at you\n")
                output_delay("you get up and try and escape but the door is locked the principal begins to laugh\n")
                output_delay(f"even more and starts to repeat you are here forever {username} HAHAHAHAHAHA!\n")
                output_delay("Please try again.\n")
                welcome_message()
                break
            elif open_door_choice == "C":
                output_delay("\nYou went through the open window leading you to the outside playground.\n")
                output_delay("escaping the monster through the open door.\n")
                output_delay(f"You escaped for now {username}\n")
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
    text_msg = """
    As you escape the classroom you notice a small dog in the corridor.
    Do you A throw your book at the dog. B turn around or C pet the dog.
    """

    output_delay(text_msg)

    while True:
        try:
            escaped_choice = input("\nPlease type either A or B or C.\n").upper()
            if escaped_choice == "A":
                output_delay("\nYou throw a science book at the dog causing an explosion\n")
                output_delay("killing the dog, well done you live to fight another day.\n")
                open_door(username)
                break
            elif escaped_choice == "B":
                output_delay("\nYou turn around and you spot an even bigger dog, before you can react\n")
                output_delay("the dog bites you try to escape but you feel yourself slowing losing control,\n")
                output_delay("you faint and as you lay there you can feel yourself getting weaker. As you slowly lose your\n")
                output_delay("soul to the underworld.\n")
                output_delay("Please try again.\n")
                welcome_message()
                break
            elif escaped_choice == "C":
                output_delay("\nYou pet the dog and the dog turns around and bites you,\n")
                output_delay("you have been lost to the underworld forever.\n")
                output_delay("Please try again.\n")
                welcome_message()
                break
            else:
                print(f"Please use the correct format by typing either A or B or C. {username}\n")
                continue
        except ValueError as e:
            print("Invalid format please try again.")


def run_game(username):
    """
    This is the first section of the game this function will allow the user 
    to read a senario and make a decision
    """
    loading_elements("Starting game....\n")
    text_msg = """
    You wake up in detention and you hear the principal in the background storming to your class room.
    You have three choices do you A go back to sleep and pretend its all just a bad dream. 
    B wait for the principal to arrive or C do you hide in the cupboard away from the principal?\n"""
    output_delay(text_msg)

    while True:
        try:
            
            first_choice = input(f"\nPlease type either A or B or C pick carefully {username}\n").upper()
            if first_choice == "A":
                output_delay("\nYou go back to sleep and the principal rushes in and throws a slice of pizza at your head. which is\n")
                output_delay("a massive fear of yours, you faint and die please try again\n")
                welcome_message()
                break
            elif first_choice == "B":
                output_delay("\nYou hide in the cupboard and watch the principal storm into the classroom after searching the classroom he\n")
                output_delay(f"shortly leaves after. You have escaped for now {username}\n")
                escaped_classroom(username)
                break
            elif first_choice == "C":
                output_delay("\nYou wait for the principal who has backup one of your biggest fears a maths test.\n")
                output_delay("You do your best but you fail the maths test, the principal laughs sniggering at you\n")
                output_delay("repeating you will remain here forever HAHAHAHAHA!\n")
                output_delay("Please try again.\n")
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
    loading_elements("\nInstructions loading....\n")

    text_msg = """
    Into Your Mind is a text based action adventure game where your decisions really matter.
    During the game you will recieve a situation where your answer matters, you will select your options by either typing A or B or C.
    Depending on the situation you find yourself in think carefully as the wrong answer could mean Game Over.
    If you would like to leave the game early at any point you can type EXIT to leave the application.
    """
    output_delay(text_msg)
    while True:
        try:
            start = input("\nPlease type either A to start the game or B to return to the main menu\n").upper()
            if start == "A":
                run_game(username)
                break
            elif start == "B":
                intro(username)
                break
            else:
                output_delay("\nPlease enter the correct format by either typing A or B")
        except ValueError as e:
            output_delay("Invalid format please use the correct format")
            

def intro(username):
    """
    This function will intro the user to the game 
    allowing them to view the instructions or start the game
    """

    output_delay(f"\nWelcome to Into Your Mind {username} if you would like to Start the game type A or if you would like to view the instructions type B")

    while True:
        try:
            intro_msg = input("\nPlease type either A or B\n").upper()
            if intro_msg == "A":
                run_game(username)
                break
            elif intro_msg == "B":
                view_instructions(username)
                break
            else:
                output_delay("Please enter a valid format\n")
        except ValueError as e:
            output_delay(f"\n {e} please pick the correct one")

welcome_message()