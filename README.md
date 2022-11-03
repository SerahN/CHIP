# CHIP

This tool takes the CSV provided by the teams, generates a CHIP-0007 compatible json, calculates the sha256 of the json file and appends it to each line in the csv (as a filename.output.csv)

##Technology Used

1. Python

##Set-Up Instructions
As mentioned earlier , this is a Django project.

Please, take note of the operating system you are using as the steps may vary.

This set-up instructions aims at helping a developer get the code from the git repository to run on their system.

###Fetch git code to local machine
Follow these steps to fetch the git code to your system:

Clone this project's repository. To do this, open your code editor and choose "Clone Git Repository", then click on "Clone from GitHub", and enter `https://github.com/SerahN/CHIP.git`

Input your csv file into the code in script.py and run the program.

```
## Results
The generated json files will be located in the json folder. A new file will be created bearing a new column tagged Sha-256.


P.S.: Resources are files I used during work that are still useful to me, kindly ignore them.
```
