# CHIP

This tool takes the CSV provided by the teams, generates a CHIP-0007 compatible json, calculates the sha256 of the json file and appends it to each line in the csv (as a filename.output.csv)

## Technology Used

**Python**

## Set-Up Instructions

As mentioned earlier , this script was written with Python.

Please, take note of the operating system you are using as the steps may vary.

This set-up instructions aims at helping a developer get the code from the git repository to run on their system.

###Fetch git code to local machine
Follow these steps to fetch the git code to your system:

Clone this project's repository. To do this, open your code editor and choose "Clone Git Repository", then click on "Clone from GitHub", and enter
`https://github.com/SerahN/CHIP.git`

Run the script and you will be prompted to input type the path or name of the csv file. The standard file used here is HNGi9 CSV FILE.csv, which is in this repository.

## Output

The generated json files will be located in the Output\json folder. A new csv file will also be created bearing a new column tagged SHA-256.

P.S.: Resources are files I used during work that are still useful to me, kindly ignore them.
