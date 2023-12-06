
def welcome_message():
    """
    This function will greet the user and allow them to 
    enter there first name
    """

    print("Welcome to your nightmare, the journey to madness has begun but how crazy can it truly get?")

    while True:
        username = input("What is your name?\n")

        if not username:
            print("Please enter your name\n")
        else:
            intro()
            break

def run_game():
    print("running game")

def view_instructions():
    print("Viewing instructions")
    """
    This function will display the instructions to the user
    teaching them how the game works and any key information
    they will need while playing the game
    """

    print("Instructions")
    print( "Into Your Mind is a text based action adventure game where your decisions really matter")
    print("During the game you will recieve a situation where your answer matters you will select your options by either typing A or B or C")
    print("Depending on the situation you find yourself in think carefully as the wrong answer could mean Game Over")
    print("If you would like to leave the game early at any point you can type EXIT to leave the application")

    while True:
        try:
            start = input("Please type either A to start the game or B to return to the main menu\n").upper()
            if start == "A":
                run_game()
                break
            elif start == "B":
                intro()
                break
            else:
                print("\nPlease enter the correct format by either typing A or B")
        except ValueError as e:
            print("Invalid format please use the correct format")
            

def intro():
    """
    This function will intro the user to the game 
    allowing them to view the instructions or start the game
    """

    print("Welcome to Into Your Mind if you would like to Start the game type A or if you would like to view the instructions type B")

    while True:
        try:
            intro_msg = input("Please type either A or B\n").upper()
            if intro_msg == "A":
                run_game()
                break
            elif intro_msg == "B":
                view_instructions()
                break
            else:
                print("Please enter a valid format\n")
        except ValueError as e:
            print(f"\n {e} please pick the correct one")


welcome_message()