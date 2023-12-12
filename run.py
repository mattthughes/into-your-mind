import time
import os
import sys


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

        if not username:
            print("Please enter your name.\n")
        else:
            intro(username)
            break


def end(username):
    clear()
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
    text_msg = """
    The imposter has escaped and you are free to
    either A fight this imposter  or B go home.
    """

    final_choice_a = """
    You confront yourself and fight with everything you
    have. As you are about to defeat this evil version
    of you wake up, all the students around you look
    mortified. As they notice the tears running down
    your face the principal walks in and asks if you
    are okay. As you look down at your notepad that
    'real' battle you were supposdly in has ended
    and was all just a dream. You begin to turn
    the pages extremley quickly, you notice every
    decision you thought you made was all part
    of your imagination.
    """

    final_choice_b = """
    You chose to go home as you enter your house
    your parents are just sitting there, as you
    try and talk to them they just ignore you,
    pretending you do not exist. You try to go
    to sleep but cannot sleep. All the fears you
    have ever had come to life before you. As
    you try to escape you are smothered by the
    monsters. As you are slowly fading you notice
    in the distance the imposter sniggering at you
    as they repeat HAHAHAHA YOU ARE TRAPPED FOREVER!
    You have been trapped in the underworld forever.
    """

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
    text_msg = f"""
    You cannot believe what you are seeing, this can't be right
    Do you A go and confront this small figure. B fight this figure
    or C do you run away. How brave are you {username}?
    """

    figure_choice_a = """
    You confront the small figure, and he laughs at you, begins to
    explain that he is the leader of this underworld and once he has
    dealt with you. He will be free to plague all of humanity escaping
    the underworld, you are unprepared for this and the imposter
    kills you escaping the underworld.
    """

    figure_choice_b = """
    You choose to fight the imposter catching them off guard
    it's a hellacious battle but you survive for now.
    """

    figure_choice_c = """
    You chose to run away the imposter smiles to themselves
    and begins to chase you. As you escape the police station
    you are hit by a car, as you lay there slowly dying, before
    you pass you hear a faint laugh in the distance, you can't
    believe what you are seeing it's the principal from the school
    cackling as they drive past your lifeless corpse.
    """

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
    text_msg = """
    You are in the police station waiting for your parents
    as you wait for your parents, you hear a loud scream.
    Do you A hide in the station or B wait for your parents or
    C go and see what the scream was.
    """

    output_delay(text_msg)

    inside_choice_a = """
    You hid away from the screaming creature but the police
    officer grabs you from underneath the chair, without
    hesitation the police officer fires his gun at you,
    he kills you, proving you cannot trust anyone in this
    world.
    """

    inside_choice_b = """
    You waited for your parents and the large creature has
    broken free, the creature grabs you as they escape taking
    you with them,killing you in the process.
    """

    inside_choice_c = """
    You are brave and go to see what the scream was, and its
    a very small figure, you cannot believe your eyes it's
    you.....
    """

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
    text_msg = """
    As you are walking home you hear a police siren in the background.
    Do you A wait for the police or do you B keep walking.
    """
    output_delay(text_msg)

    home_option_a = f"""
    You waited for the police and they take you
    to the police station you are safe for now
    {username}"""

    home_option_b = """
    You kept walking home as you continue walking a
    large figure appears they open a blackhole.
    Which sucks in leaving you stuck in the void
    forever
    """

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

    text_msg = """
    You find an open school bus leading you out of the school.
    Do you A go through the school bus and head out the open
    door or B hide under the bus seats?
    """
    output_delay(text_msg)

    bus_choice_a = """
    You go through the open bus and spot an exit,
    you quickly make a dash for the exit and
    escape the school. Now to find the way
    home and fast.
    """
    bus_choice_b = """
    You went through the open bus and hid under
    the seats, suddenly all the chewing gum under
    the seats has grown to the size of the school
    bus. Before you can react the chewing gum
    monster smothers you, takes your souls,
    banishing you to the underworld forever.
    """

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

    text_msg = """
    As you explore the abandoned school you notice an open door
    and an open window.
    Do you A go through the door. B slam the door shut or C go
    through the open window and escape.
    """
    door_option_a = """
    You went through the open door, were attacked
    and then eaten by an alien one of your
    biggest fears you die.
    """

    door_option_b = f"""
    You slammed the door shut and alerted the principal, he
    finds you and takes you to his office. The principal
    begins to laugh at you get up and try and escape
    but the door is locked the principal begins to laugh
    even more and starts to repeat you are
    here forever {username} HAHAHAHAHAHA!.
    """

    door_option_c = f"""
    You went through the open window leading you
    to the outside playground, escaping the
    monster through the open door. You escaped
    for now {username}
    """

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

    text_msg = """
    As you escape the classroom you notice a small dog in the corridor.
    Do you A throw your book at the dog. B turn around or C pet the dog.
    """

    escaped_choice_a = """
    You throw a science book at the dog causing an explosion
    killing the dog, well done you live to fight another day.
    """

    escaped_choice_b = """
    You turn around and you spot an even bigger dog, before you can react
    the dog bites you try to escape but you feel yourself slowing losing
    control, you faint and as you lay there you can feel yourself
    getting weaker. As you slowly lose your soul to the underworld.
    """

    escaped_choice_c = """
    You pet the dog and the dog turns around and bites you,
    you have been lost to the underworld forever.
    """
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
    text_msg = """
    You wake up in detention and you hear the principal in the
    background storming to your class room. You have three choices
    do you A go back to sleep and pretend its all just a bad dream.
    B wait for the principal to arrive or C do you hide in the cupboard
    away from the principal?\n
    """

    first_choice_a = """
    You go back to sleep and the principal rushes in and
    throws a slice of pizza at your head. which is
    a massive fear of yours, you faint and die
    """

    first_choice_b = """
    You wait for the principal who has backup one of your biggest
    fears a maths test. You do your best but you fail the maths test,
    the principal laughs sniggering at you repeating you will remain here
    forever HAHAHAHAHA!
    """

    first_choice_c = f"""
    You hide in the cupboard and watch the principal storm into the classroom
    after searching the classroom he shortly leaves after.
    You have escaped for now {username}
    """

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
