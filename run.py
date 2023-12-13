import time
import os
import sys
from scenario import scenarios


def clear():
    """
    This function is using the os.system from
    os and is using the phrase clear allowing
    me to control when the terminal clears
    making sure the terminal remains neat.
    """
    os.system("clear")


def output_delay(text_msg):
    """
    This function controls the speed output of the
    text using flush to print to the console immedaietly
    then using the time.sleep method to control the speed of the
    output
    """
    for i in text_msg:
        print(i, end="", flush=True)
        time.sleep(0.07)


def loading_elements(loading):
    """
    This function controls the speed output of the
    text using flush to print to the console immedaietly
    then using the time.sleep method to control the speed of the
    output
    """
    for i in loading:
        print(i, end="", flush=True)
        time.sleep(0.1)


def load_game_over(game_over_msg):
    for i in game_over_msg:
        print(i, end="", flush=True)
        time.sleep(0.02)


def load_game_title(title_msg):
    for i in title_msg:
        print(i, end="", flush=True)
        time.sleep(0.04)

def load_win_condition(win_msg):
    for i in win_msg:
        print(i, end="", flush=True)
        time.sleep(0.03)


def exit_program(username):
    """
    This function will exit the application
    while thanking the user for playing
    """
    clear()
    loading_elements("Exiting Game.....\n")
    output_delay(f"Thank you for playing {username}")
    sys.exit()


def game_over(username):
    clear()
    game_over_msg = """

    ██╗░░░██╗░█████╗░██╗░░░██╗  ██████╗░██╗███████╗██████╗░
    ╚██╗░██╔╝██╔══██╗██║░░░██║  ██╔══██╗██║██╔════╝██╔══██╗
    ░╚████╔╝░██║░░██║██║░░░██║  ██║░░██║██║█████╗░░██║░░██║
    ░░╚██╔╝░░██║░░██║██║░░░██║  ██║░░██║██║██╔══╝░░██║░░██║
    ░░░██║░░░╚█████╔╝╚██████╔╝  ██████╔╝██║███████╗██████╔╝
    ░░░╚═╝░░░░╚════╝░░╚═════╝░  ╚═════╝░╚═╝╚══════╝╚═════╝░
    """

    text_msg = """
    Please try again if you would like to restart the game type
    A. If you would like to return to the main menu type B or if
    you would like to exit the game type EXIT.
    """

    load_game_over(game_over_msg)

    output_delay(text_msg)

    while True:
        try:
            game_over_choice = input("Please type A or B or EXIT\n").upper()
            if game_over_choice == "A":
                run_game(username)
            elif game_over_choice == "B":
                welcome_message()
            elif game_over_choice == "EXIT":
                exit_program(username)
            else:
                output_delay("Please enter A or B or EXIT\n")
        except ValueError as e:
            output_delay("Please enter A or B or EXIT\n")


def welcome_message():
    """
    This function will greet the user and allow them to
    enter there first name
    """
    clear()

    title_intro = """

    █ █▄░█ ▀█▀ █▀█   █▄█ █▀█ █░█ █▀█   █▀▄▀█ █ █▄░█ █▀▄
    █ █░▀█ ░█░ █▄█   ░█░ █▄█ █▄█ █▀▄   █░▀░█ █ █░▀█ █▄▀
    """
    load_game_title(title_intro)

    text_msg = """
    Welcome to your nightmare, the journey to madness has begun
    but how crazy can it truly get?
    """
    output_delay(text_msg)

    while True:
        username = input("What is your name?\n")

        if not username or not username.isalpha():
            print("Please enter your name with alphabet letters.\n")
        else:
            intro(username)
            break


def end(username):
    clear()

    win_msg = """
    
    ██████████████████████████████████████████████████████████████████████████████████████████████████████████████
    █░░░░░░░░██░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██░░░░░░████░░░░░░██████████░░░░░░█░░░░░░░░░░█░░░░░░██████████░░░░░░█
    █░░▄▀▄▀░░██░░▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░████░░▄▀░░██████████░░▄▀░░█░░▄▀▄▀▄▀░░█░░▄▀░░░░░░░░░░██░░▄▀░░█
    █░░░░▄▀░░██░░▄▀░░░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░████░░▄▀░░██████████░░▄▀░░█░░░░▄▀░░░░█░░▄▀▄▀▄▀▄▀▄▀░░██░░▄▀░░█
    ███░░▄▀▄▀░░▄▀▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░████░░▄▀░░██████████░░▄▀░░███░░▄▀░░███░░▄▀░░░░░░▄▀░░██░░▄▀░░█
    ███░░░░▄▀▄▀▄▀░░░░███░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░████░░▄▀░░██░░░░░░██░░▄▀░░███░░▄▀░░███░░▄▀░░██░░▄▀░░██░░▄▀░░█
    █████░░░░▄▀░░░░█████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░████░░▄▀░░██░░▄▀░░██░░▄▀░░███░░▄▀░░███░░▄▀░░██░░▄▀░░██░░▄▀░░█
    ███████░░▄▀░░███████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░████░░▄▀░░██░░▄▀░░██░░▄▀░░███░░▄▀░░███░░▄▀░░██░░▄▀░░██░░▄▀░░█
    ███████░░▄▀░░███████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░████░░▄▀░░░░░░▄▀░░░░░░▄▀░░███░░▄▀░░███░░▄▀░░██░░▄▀░░░░░░▄▀░░█
    ███████░░▄▀░░███████░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░████░░▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀░░█░░░░▄▀░░░░█░░▄▀░░██░░▄▀▄▀▄▀▄▀▄▀░░█
    ███████░░▄▀░░███████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░████░░▄▀░░░░░░▄▀░░░░░░▄▀░░█░░▄▀▄▀▄▀░░█░░▄▀░░██░░░░░░░░░░▄▀░░█
    ███████░░░░░░███████░░░░░░░░░░░░░░█░░░░░░░░░░░░░░████░░░░░░██░░░░░░██░░░░░░█░░░░░░░░░░█░░░░░░██████████░░░░░░█
    ██████████████████████████████████████████████████████████████████████████████████████████████████████████████
    """

    load_win_condition(win_msg)


    text_msg = f"""
    Congratulations you have beaten the game,
    I guess its not what you expected have you
    really escaped the imposter or is he still
    out there planning his revenge to once and
    for all take over the world. Have you really
    escaped or did he let you escape, or was it all
    just a bad dream I guess that is up to you {username}
    to decide. If you would like to play the game again
    type A or if you would like to exit type EXIT
    """
    output_delay(text_msg)

    while True:
        try:
            end_choice = input("Please type either A or EXIT\n").upper()
            if end_choice == "A":
                run_game(username)
                break
            elif end_choice == "EXIT":
                exit_program(username)
                break
            else:
                output_delay("Please type either A or EXIT\n")
                continue
        except ValueError as e:
            output_delay(f"{e} Please type either A or EXIT\n")


def final_battle(username):
    clear()
    text_msg = scenarios.get("final_battle")["message"]

    final_choice_a = scenarios.get("final_battle")["final_choice_a"]

    final_choice_b = scenarios.get("final_battle")["final_choice_b"]

    output_delay(text_msg)

    while True:
        try:
            final_choice = input("Please type either A or B\n").upper()
            if final_choice == "A":
                output_delay(final_choice_a)
                end(username)
                break
            elif final_choice == "B":
                output_delay(final_choice_b)
                game_over(username)
                break
            elif final_choice == "EXIT":
                exit_program(username)
                break
            else:
                output_delay("Please type either A or B\n")
                continue
        except ValueError as e:
            output_delay(f"{e} Please type either A or B\n")


def small_figure(username):
    clear()
    text_msg = scenarios.get("small_figure")[f"message"]

    figure_choice_a = scenarios.get("small_figure")["figure_choice_a"]

    figure_choice_b = scenarios.get("small_figure")["figure_choice_b"]

    figure_choice_c = scenarios.get("small_figure")["figure_choice_c"]

    output_delay(text_msg)

    while True:
        try:
            figure_choice = input("Please type A or B or C").upper()
            if figure_choice == "A":
                output_delay(figure_choice_a)
                game_over(username)
                break
            elif figure_choice == "B":
                output_delay(figure_choice_b)
                final_battle(username)
                break
            elif figure_choice == "C":
                output_delay(figure_choice_c)
                game_over(username)
                break
            elif figure_choice == "EXIT":
                exit_program(username)
                break
            else:
                output_delay("Please enter either A or B or C\n")
                continue
        except ValueError as e:
            output_delay(f"{e} Please use the correct format\n")


def inside_station(username):
    clear()
    text_msg = scenarios.get("inside_station")["message"]

    output_delay(text_msg)
    inside_choice_a = scenarios.get("inside_station")["inside_choice_a"]

    inside_choice_b = scenarios.get("inside_station")["inside_choice_b"]

    inside_choice_c = scenarios.get("inside_station")["inside_choice_c"]

    while True:
        try:
            inside_choice = input("Please type A or B or C\n").upper()
            if inside_choice == "A":
                output_delay(inside_choice_a)
                game_over(username)
                break
            elif inside_choice == "B":
                output_delay(inside_choice_b)
                game_over(username)
                break
            elif inside_choice == "C":
                output_delay(inside_choice_c)
                small_figure(username)
                break
            elif inside_choice == "EXIT":
                exit_program(username)
                break
            else:
                output_delay("Please type A or B or C\n")
                continue
        except ValueError as e:
            output_delay("Please type A or B or C\n")


def journey_home(username):
    """
    This function will inform the user of the next senario giving them
    two options to pick from
    """
    clear()
    text_msg = scenarios.get("journey_home")["message"]

    output_delay(text_msg)
    home_option_a = scenarios.get("journey_home")["home_option_a"]
    home_option_b = scenarios.get("journey_home")["home_option_b"]

    while True:
        try:
            home_choice = input("\nPlease type either A or B\n").upper()
            if home_choice == "A":
                output_delay(home_option_a)
                inside_station(username)
                break
            elif home_choice == "B":
                output_delay(home_option_b)
                game_over(username)
                break
            elif home_choice == "EXIT":
                exit_program(username)
            else:
                output_delay("\nPlease type either A or B.\n")
                continue
        except ValueError as e:
            print(f"{e} please use the correct format\n")


def abandoned_bus(username):
    """
    This function will inform the user of the next senario giving them
    two options to pick from
    """
    clear()

    text_msg = scenarios.get("abandoned_bus")["message"]
    output_delay(text_msg)
    bus_choice_a = scenarios.get("abandoned_bus")["bus_choice_a"]
    bus_choice_b = scenarios.get("abandoned_bus")["bus_choice_b"]

    while True:
        try:
            bus_choice = input("\nPlease type either A or B\n").upper()
            if bus_choice == "A":
                output_delay(bus_choice_a)
                journey_home(username)
                break
            elif bus_choice == "B":
                output_delay(bus_choice_b)
                game_over(username)
                break
            elif bus_choice == "EXIT":
                exit_program(username)
            else:
                print(f"invalid format {username} Please type either A or B\n")
                continue
        except ValueError as e:
            print("Invalid format please type either A or B\n")


def open_door(username):
    """
    This function id the third section of the game
    allowing the user to pick one out of three options
    """
    clear()

    text_msg = scenarios.get("open_door")["message"]
    door_option_a = scenarios.get("open_door")["door_option_a"]
    door_option_b = scenarios.get("open_door")["door_option_b"]
    door_option_c = scenarios.get("open_door")["door_option_c"]
    output_delay(text_msg)

    while True:
        try:
            door_choice = input("\nPlease type either A or B or C\n").upper()
            if door_choice == "A":
                output_delay(door_option_a)
                game_over(username)
                break
            elif door_choice == "B":
                output_delay(door_option_b)
                game_over(username)
                break
            elif door_choice == "C":
                output_delay(door_option_c)
                abandoned_bus(username)
                break
            elif door_choice == "EXIT":
                exit_program(username)
                break
            else:
                output_delay("Please type either A or B or C.\n")
                continue
        except ValueError as e:
            print(f"{e} please fill in the right format\n")


def escaped_classroom(username):
    """
    This function is the second section of the game, this allows the user
    to pick one out of three options
    """
    clear()
    text_msg = scenarios.get("escaped_classroom")["message"]
    escaped_choice_a = scenarios.get("escaped_classroom")["escaped_choice_a"]
    escaped_choice_b = scenarios.get("escaped_classroom")["escaped_choice_b"]
    escaped_choice_c = scenarios.get("escaped_classroom")["escaped_choice_c"]
    output_delay(text_msg)

    while True:
        try:
            escaped_choice = input("\nPlease type A or B or C.\n").upper()
            if escaped_choice == "A":
                output_delay(escaped_choice_a)
                open_door(username)
                break
            elif escaped_choice == "B":
                output_delay(escaped_choice_b)
                game_over(username)
                break
            elif escaped_choice == "C":
                output_delay(escaped_choice_c)
                game_over(username)
                break
            elif escaped_choice == "EXIT":
                exit_program(username)
                break
            else:
                print(f"Please type either A or B or C. {username}\n")
                continue
        except ValueError as e:
            print("Invalid format please try again.\n")


def run_game(username):
    """
    This is the first section of the game this function will allow the user
    to read a senario and make a decision
    """
    clear()
    loading_elements("Starting game....\n")
    first_choice_a = scenarios.get("classroom_scenario")["first_choice_a"]
    first_choice_b = scenarios.get("classroom_scenario")["first_choice_b"]
    first_choice_c = scenarios.get("classroom_scenario")["first_choice_c"]
    text_msg = scenarios.get("classroom_scenario")["message"]
    output_delay(text_msg)

    while True:
        try:
            first_choice = input("Please type A or B or C\n").upper()
            if first_choice == "A":
                output_delay(first_choice_a)
                game_over(username)
                break
            elif first_choice == "B":
                output_delay(first_choice_b)
                game_over(username)
                break
            elif first_choice == "C":
                output_delay(first_choice_c)
                escaped_classroom(username)
                break
            elif first_choice == "EXIT":
                exit_program(username)
                break
            else:
                print("Please enter the correct format either A or B or C\n")
                continue
        except ValueError as e:
            print(f"please enter the correct format user {username}")


def view_instructions(username):
    """
    This function will display the instructions to the user
    teaching them how the game works and any key information
    they will need while playing the game
    """
    clear()
    loading_elements("\nInstructions loading....\n")
    text_msg = """
    Into Your Mind is a text based action adventure game
    where your decisions really matter. During the game
    you will recieve a situation where your answer matters,
    you will select your options by either typing A or B or C.
    Depending on the situation you find yourself in think carefully
    as the wrong answer could mean Game Over.
    If you would like to leave the game early at any point
    you can type EXIT to leave the application.
    Type A to start the game or Type B to return to
    the main menu
    """
    output_delay(text_msg)
    while True:
        try:
            start = input("\nPlease type either A or B\n").upper()
            if start == "A":
                run_game(username)
                break
            elif start == "B":
                intro(username)
                break
            elif start == "EXIT":
                exit_program(username)
            else:
                output_delay("\nPlease enter either A or B\n")
        except ValueError as e:
            output_delay("Invalid format please use the correct format\n")


def intro(username):
    """
    This function will intro the user to the game
    allowing them to view the instructions or start the game
    """
    clear()
    text_msg = f"""
    Welcome to Into Your Mind {username} if you would like to Start the game
    type A or if you would like to view the instructions type B
    """
    output_delay(text_msg)

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
            output_delay(f"\n {e} please pick the correct one\n")


welcome_message()
