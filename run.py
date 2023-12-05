
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
            intro(username)
            break

def run_game():
    print("running game")

def view_instructions():
    print("Viewing instructions")

def intro(username):
    """
    This function will intro the user to the game 
    allowing them to view the instructions or start the game
    """

    print("Welcome to Into Your Mind if you would like to Start the game type A or if you would like to view the instructions type B")

    while True:
        try:
            start = input("Please type either A or B\n")
            if start == "A".lower():
                run_game()
                break
            elif start == "B".lower():
                view_instructions()
                break
            else:
                print("Please enter a valid format\n")
        except ValueError:
            print("\n Invalid format please pick the correct one")


welcome_message()