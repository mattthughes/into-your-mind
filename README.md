![Into Your Mind title](docs/into-your-mind-title.png)

# Into Your Mind

Welcome to Into Your Mind this app was created with Python and deployed with Heroku. This game was designed to lead players through the madness option text based game called into your mind, this game will have different options allowing the player to decide where they would like to go next, but pick carefully as picking the wrong option can result in game over.

## CONTENTS

- [Into Your Mind](#into-your-mind)
    - [CONTENTS](#contents)
    - [Project Goals](#project-goals)
        - [Client Goals](#client-goals)
        - [User Goals](#user-goals)
        - [Frequent User Goals](#frequent-user-goals)
        - [Future Implementations](#future-implementations)
    - [Design](#design)
        - [Flow Chart](#flow-chart)
            - [Creative Decisions](#creative-decisions)
    - [Key Features](#key-features)
        - [Welcome Message](#welcome-message)
        - [Wrong Format Welcome Message](#wrong-format-welcome-message)
        - [Intro Message](#intro-message)
        - [Instructions](#instructions)
        - [Different Scenarios](#different-scenarios)
        - [Correct Answers](#correct-answers)
        - [Wrong Answers](#wrong-answers)
        - [Game Over Screen](#game-over-screen)
        - [Exit Screen](#exit-screen)
        - [Wrong Format](#wrong-format)
        - [Congratulations screen](#congratulations-screen)
    - [Languages](#languages)
    - [Frameworks and tools](#frameworks--tools)
    - [Deployment](#deployment)
        - [How to deploy](#how-to-deploy)
        - [How to fork](#how-to-fork)
        - [How to deploy on heroku](#how-to-clone)
    - [Credits](#credits)
        - [Media](#media)
        - [Code](#code)
        - [Content](#content)
        - [Acknowledgements](#acknowledgements)

[Live project](https://into-your-mind-f09dce66f4f1.herokuapp.com/)

## Project Goals

### Client Goals

* Build a text based adventure game with user input.
* Make sure users are able to leave the application at any point
* The text based adventure game should be orginal and should be completable.

### User Goals

* I would like to view the instructions to understand how to play the game.
* I would like to be able to enter my own name to create my own character.
* I would like to be able to make clear decisions that have an impact on the game.
* I like story driven text based adventures which have a clear explanation on the world and its surroundings.

### Frequent user goals

* I would like my decisions to have importance with clear descriptions on what happens next.
* I would like to restart or exit the game at any point if I was to make a wrong decision.
* I Would like to return to the main menu at any time to view any further instructions I may have missed.


### Future Implementations

* In the future I will look at add a timer to increase the tension during gameplay.
* I would like to add a scoreboard so users are able to compete against friends and family
* I would like to add further scenarios to make the game even more challenging.

## Design

### Flow Chart 

This is how into your mind will work each decision the user makes will lead to a specific senario whether that is viewing the instructions or just progressing in the game each decision the user makes has an outcome. This flow chart has allowed me to outline the logic I am looking to follow which means during production there will be no logic gaps and everything will work as I intended.

![Flow chart logic part 1](docs/into-your-mind-logic-part-1.png)
![Flow chart logic part 2](docs/into-your-mind-logic-part-2.png)
![Flow chart full diagram](docs/into-your-mind-logic-full-flow-chart.png)

#### Creative decisions

* For the flow chart I made some decisions on how I wanted the story to go for example, this character I have created in this universe is a scared child which falls asleep in detention so it is natural for the character to hide. 

* Scenario two is where the character is a bit stumped as they saw the principle storm into the classroom, smashing desks out of the way trying to find you, this next creative choice made sense after what had just gone on before it.

* Scenario three you choose to escape through an open window the other two options felt obvious and did not fit the characters story arc.

* Scenario four you choose to quickly escape the bus rather than hiding like you did in the first act, which shows the progression of the character which is what I intended.

* Scenario five you choose to wait for the police rather than trying to escape as surely the craziness just existed in the school right?

* Scenario six you choose to be brave and see what the scream was this again made sense for the character arc. As you have been on choosing not to hide but face your fears.

* Scenario seven you choose to fight the imposter, the game has been building towards this moment. I made this choice as this fit the character arc I was looking to create.

* Final Scenario you choose to stop the imposter once and for all. This decision was made as the character letting the imposter escape did not fit with the rest of the story being brave and taking a chance to be a hero did which is why this decision was made.


## Key Features

### Welcome Message

* This element will allow users to enter there first name. Which allows them to create there own character, making the experience more personalised for themselves.

![Welcome Message](docs/welcome-msg.png)

### Wrong format Welcome Message

* This will be shown if the user doesn't enter anything. An error message will appear asking the user to enter there name.

![Welcome Message error](docs/incorrect-format-welcome-msg.png)

### Text delay 

* This element will be showcased during every text output, this has been included to improve readability as the print function
would just display the whole text making this difficult to read for the user which this feature fixed.

![Text delay gif](gifs/text-delay.gif)

### Intro Message 

* This intro message will greet the user with the name they entered. After this the intro message will continue allowing the user to either enter A to start the game or B to view the instructions, allowing the user to take there time before starting the game.

![Intro message](docs/intro-msg.png)

### Wrong Format Intro Message

* This will be shown if the user doesn't enter the correct format. An error message will appear asking the user to enter the correct input while the statement will repeat asking the user to enter either A to start the game or B to view the instrctions.

![Wrong Format Intro Message](docs/wrong-format-intro.png)

### Instructions

* This element will teach the user how  to play the game informing them the rules of the game, teaching them about how to answer the different scenarios that are presented to the user. The instructions will also contain valuable information for the user such as informing the user they are able to leave the game at any time by typing exit. This will all be showcased in the instructions element, making sure the user does not get frustrated and understands the game before starting.

![Instructions](docs/instructions-into-your-mind.png)

### Different Scenarios 

* This element is the different scenarios that will appear depending on where the user finds themsevles in the game. Different Scenarios will have different requirements where some will have three options, whereas others will have two. For each scenario there will be only one correct answer meaning the wrong answer will mean game over, teaching the user to think carefully before confirming there answer. Down below are three different scenarios at different points in the game showing the user what they could expect when playing Into Your Mind.

![Scenario one](docs/scenario-one-into-your-mind.png)

![Scenario example two](docs/different-scenario-two.png)

![Scenario example three](docs/different-scenario-three.png)

### Correct Answers 

* This element will show the result of answering a scenario correctly moving onto the next stage of the game.

![Correct Answers](docs/correct-answer-into-your-mind.png)

### Wrong Answers

* This element will show the result of answering a scenario loading the game over screen for the user informing them that the answer is incorrect and to try again.

![Wrong Answers](docs/wrong-answer-into-your-mind.png)

### Game Over Screen

* This element will be shown to the user when the user gets an answer wrong, with the message you died being shown. After this message appears there will also be a message informing the user to either type A to restart the game and try again. The user can also type B to go back to the Main Menu. The user could also type exit to exit the application altogether. After exiting the application the user can click run program to restart the application from the beginning starting from scratch.

![Game over screen](docs/game-over-into-your-mind.png)

### Exit screen 

* This element will be shown if at any point the user types in EXIT. To ensure errors do not occur I have also used the .upper method to make sure errors do not occur if the user enters exit in lowercase rather than in uppercase. The exit message will thank the user for playing the game while also exiting the application altogether. If the user would like to restart the application they can simply click the run program button.

![Exit screen](docs/exit-program.png)

### Wrong Format 

* This element will be shown if the user does not enter either A or B or C or even exit depending on the different scenario. If the user was to enter a number this error message would be shown. If A or B or C or exit have not been entered this same error message will appear. This will give the user clear visual feedback in what they need to do, removing any unneccesary frustration the user may have had, if this was not outlined clearly.

![Wrong Format scenarios](docs/wrong-format-scenario.png)

### Congratulations screen

* This element will be shown if the user has answered every scenario correctly. This screen will inform the user of there success providing further key story information, they would have not recieved unless they had completed the game. Upon completetion the user will be asked to type either A to play again or to type EXIT to exit the applicaton altogether.

![Congratulations screen](docs/winning-screen.png)

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

This site is deployed using GitHub Pages - [Into Your Mind](https://github.com/mattthughes/into-your-mind)

To deploy the site using GitHub Pages follow the following steps:

1. Login or signup to GitHub
2. Go to the repository for this project [mattthughes/into-your-mind](https://github.com/mattthughes/into-your-mind)
3. Click the settings button.
4. Select pages in the left hand navigation menu
5. From the source dropdown select main branch changing this from root to main and then press save.
6. After this the site has been deployed.

### How to fork

1. Log in or sign u to GitHub.
2. Go to the repository for this project [mattthughes/into-your-mind](https://github.com/mattthughes/into-your-mind)
3. Click the Fork button on the right corner to fork the project.

### How to deploy on heroku

## Credits 

### Media 

* You died, Game Over text taken from [FSymbols](https://fsymbols.com/)

#### Code

* The text delay functions were inspired by geeksforgeeks and customised to my projects needs [Text Delay function](https://www.geeksforgeeks.org/how-to-add-time-delay-in-python/)

* The clear function was inspired by Dev.to and was customised to my projects needs [Clear function](https://dev.to/lewiskori/how-to-clear-screen-in-python-terminal-10el)
#### Content

* All content was written by Matthew Hughes

#### Acknowledgements

* I would like to thank my mentor Graeme for his help during our sessions, which helped me make changes and improvements to the project where neccessary.
* I would like to thank my friends and family, who helped me with testing such as reporting any bugs they did encounter while playing the game. This was very helpful when fixing bugs.