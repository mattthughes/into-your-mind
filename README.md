# Into Your Mind

Welcome to Into Your Mind this app was created with Python and deployed with Heroku. This game was designed to lead players through the madness option text based game called into your mind, this game will have different options allowing the player to decide where they would like to go next, but pick carefully as picking the wrong option can result in game over.

## CONTENTS

## Project Goals

### User Stories 

* I would like to view the instructions to understand how to play the game.
* I would like to be able to enter my own name to create my own character.
* I would like to be able to make clear decisions that have an impact on the game.
* I would like my decisions to have importance with clear descriptions on what happens next.
* I would like to restart or exit the game at any point if I was to make a wrong decision.
* I Would like to return to the main menu at any time to view any further instructions I may have missed.
* I like story driven text based adventures which have a clear explanation on the world and its surroundings. 

## Flow Chart 


## Key Features

### Welcome Message

* This element will allow users to enter there first name. Which allows them to create there own character, making the experience more personalised for themselves.

## Languages 

## Frameworks & Tools 

## Deployment 

### How to deploy 

### How to fork

### How to clone

## Testing 

### Solved Bugs

* Fixed a bug where the while loop at the beginning continued to loop or was only printing the valid statement once with the break keyword. In order to fix this I used the try and except methods in the while loop, which checked to see if the conditions were met. If they were the code would run, unless there was a value error which would then  print out the else statement. Asking the user to use the correct format the loop would keep running until the else statement was met.
* Fixed a bug where the user couldn't enter a lowercase value. In order to fix this I added the .upper method to the start variable, which converted each string input to an uppercase value which passed the if validation fixing this issue.
* Fixed a bug where username was not defined and could not be accessed in other functions apart from the welcome message function where the username variable was declared. To fix this I added the username paramater for every function other than the welcome message function, which allowed me to access the username variable in other functions.
* Fixed a bug where the first selection would keep repeating when the answer was correct. In order to fix this I added the continue keyword to the else statement which fixed this issue.
* Fixed a bug where the output delay was repeating removed the output delay from the while true statement and adjusted the format of the text message to improve readability for the user.
* Fixed a bug where the abandoned bus kept repeating to fix this, I added the break keyword to the if statements if that specific condition was met. Whereas I added the continue keyword to the else statement to stop the loop running.

## Credits 

### Media 

#### Code

#### Content 

#### Acknowledgements