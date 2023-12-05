
def welcome_message():
    print("Welcome to your nightmare, the journey to madness has begun but how crazy can it truly get?")

    while True:
        username = input("What is your name?")

        if not username:
            print("Please enter your name")
        else:
            break