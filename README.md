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

This is how into your mind will work each decision the user makes will lead to a specific senario whether that is viewing the instructions or just progressing in the game each decision the user makes has an outcome. This flow chart has allowed me to outline the logic I am looking to follow which means during production there will be no logic gaps and everything will work as I intended.

![Flow chart logic part 1](docs/into-your-mind-logic-part-1.png)
![Flow chart logic part 2](docs/into-your-mind-logic-part-2.png)
![Flow chart full diagram](docs/into-your-mind-logic-full-flow-chart.png)

## Key Features

### Welcome Message

* This element will allow users to enter there first name. Which allows them to create there own character, making the experience more personalised for themselves.

### Intro Message 

* This intro message will greet the user with the name they entered. After this the intro message will continue allowing the user to either enter A to start the game or B to view the instructions, allowing the user to take there time before starting the game.

### Instructions

* This element will teach the user how  to play the game informing them the rules of the game, teaching them about how to answer the different scenarios that are presented to the user. The instructions will also contain valuable information for the user such as informing the user they are able to leave the game at any time by typing exit. This will all be showcased in the instructions element, making sure the user does not get frustrated and understands the game before starting.

### Different Scenarios 

* This element is the different scenarios that will appear depending on where the user finds themsevles in the game. Different Scenarios will have different requirements where some will have three options, whereas others will have two. For each scenario there will be only one correct answer meaning the wrong answer will mean game over, teaching the user to think carefully before confirming there answer. Down below are three different scenarios at different points in the game showing the user what they could expect when playing Into Your Mind.

### Correct Answers 

* This element will show the result of answering a scenario correctly moving onto the next stage of the game. 

### Wrong Answers

* This element will show the result of answering a scenario loading the game over screen for the user informing them that the answer is incorrect and to try again.

### Game Over Screen

* This element will be shown to the user when the user gets an answer wrong, with the message you died being shown. After this message appears there will also be a message informing the user to either type A to restart the game and try again. The user can also type B to go back to the Main Menu. The user could also type exit to exit the application altogether. After exiting the application the user can click run program to restart the application from the beginning starting from scratch.

### Exit screen 

* This element will be shown if at any point the user types in EXIT. To ensure errors do not occur I have also used the .upper method to make sure errors do not occur if the user enters exit in lowercase rather than in uppercase. The exit message will thank the user for playing the game while also exiting the application altogether. If the user would like to restart the application they can simply click the run program button.

### Wrong Format 

* This element will be shown if the user does not enter either A or B or C or even exit depending on the different scenario. If the user was to enter a number this error message would be shown. If A or B or C or exit have not been entered this same error message will appear. This will give the user clear visual feedback in what they need to do, removing any unneccesary frustration the user may have had, if this was not outlined clearly.

### Congratulations screen

* This element will be shown if the user has answered every scenario correctly. This screen will inform the user of there success providing further key story information, they would have not recieved unless they had completed the game. Upon completetion the user will be asked to type either A to play again or to type EXIT to exit the applicaton altogether.

## Languages 

* Python

## Frameworks & Tools 

- [Git Hub](https://github.com/)
- [Git](https://git-scm.com/)
- [Code Anywhere](https://codeanywhere.com/solutions/collaborate)
- [Fsy symbols](https://fsymbols.com/text-art/)
- [Heroku](https://www.heroku.com/)
- [Python Validator](https://pep8ci.herokuapp.com/#)

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
* After validation I noticed many bugs where the letter count had exceeded the maximum allowance and there were many white spaces which were being shown as errors. In order to fix this, I changed the formatting for the whole run.py document. Which involved removing extra white spaces, making sure the letter count was not exceeding the maximum allowance. While also adding in extra spaces, to ensure there was enough spaces between functions, doing all of this fixed these issues, with the code passing the validation checker with no bugs.
* Adjusted senario selection bugs where the user would enter an input and the wrong senario was being showcased in order to fix this I made some changes to the text message senario making sure the correct senarios were being shown.
* Fixed a bug where figure choice c was being reassigned before being defined in the small figure function in order to fix this I removed one equals sign which fixed this issue.
* Fixed exit bug by adding in the paramater username for all functions.
* Fixed game over bugs by adjusting the speed of the load game over function to improve readability for the user.

## Credits 

### Media 

#### Code

#### Content 

#### Acknowledgements