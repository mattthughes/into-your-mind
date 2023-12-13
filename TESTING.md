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
* Fixed a bug where the user could input numbers or special characters into the name field. To fix this I used the or not operator and the isalpha method to make sure the input being entered is a string and not a float, int or any special characters which fixed this issue.
* Fixed scenario bugs when trying to import the dictionary, an error appeared stating that none is not an object. In order to access the nested dictionary I first used the get method to get the dictionary scenarios. Then used the brackets to get the nested object scenario one and then square brackets to get the child. Which fixed these bugs, allowed me to access the nested dictionary.
* Fixed win message but, the text imported was much bigger than the terminal, to fix this I changed the image to fit the terminal which fixed this issue.

### Manual Testing 

`Intro screen` 

**Element**|**Expected Outcome**|**Testing Performed**|**Result**|**Pass/Fail**
:-----:|:-----:|:-----:|:-----:|:-----:
Intro Message|Intro message to show when program runs|Run Program|Intro message shown|Pass
Intro Message (input = none)|Please enter your name to appear|Pressed enter|Please enter your name shown|Pass
Intro Message (completed)|Welcome message to appear|Entered name|Welcome Message appeared|Pass
Welcome message (none)|Please enter a valid format message|Pressed enter|Please enter a valid format|Pass
Welcome Message (A)|Game to start with first senario|Typed A|Game started with first senario|Pass
Welcome Message (B)|Instructions to load informing user how to play|Typed B|Instructions loaded|Pass
Instructions(none)|Please enter either A or B loaded|Entered nothing|Please enter either A or B loaded|Pass
Instructions(A)|Game to start with first senario|Typed A|Game started with first senario|Pass
Instructions(B)|Main menu to load|Typed B|Main Menu Loaded|Pass
Instructions(Exit)|Message to thank the user for playing, to exit application|Typed Exit|Message to thank the user for playing, to exit application shown|Pass
