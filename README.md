# Testing Jenny
## Overview
The problem is calculate the hours worked by the employments. The data is loaded in .txt file. The code parse an argument --file with file's name, considerate the location of this file must be at same level of README.md.
For made this solution I have made some consideration:
- If a line have a wrong format , cli must show an error message.
- If hours have an invalid value, cli must show an error message.
- If time of hour exit is less than hour entrance, cli must show an error and don't calculate the salary for this person.
- I have considerate if a person worked more than 30 minutes the solution considerate it as complete hour in another case this minutes would be avoid from total.

In the code I use datetime library for made operation with the time, also I have use exception for detect error in the input data.

## Explanation
Main funtion is the core of the solution. At start, the file name is parse as an argument then the code read and save the data of this file.
For each line the code extract the name and a list with the hours worked for a person, then for each day the code check time and format before call "divide_in_range" function to get the among of money by day. The system sum all the values to get the total amount to pay. 

divide_in_range function:
This function check if the entry hour is inside the range, otherwise add 0 value in a array. If entry and exit hour are inside range, it would made a subtract and saved result in an array, in another case the system subtract range limit of entry hour and save result in an array also change entry hour with range limit for the next loop.
In subtract calculation the system round hours so if a person work more than 30 minutes it's considerate a complete hour. Also if exit hour is 0:00 the system add a day in order to considerate it a 0:00 of the next day.
Finally there are an array with the hours worked by range and another with price for range so, the code multiplicate two array element by element and sum all for get the total to pay by day.

I have made some test for divide_in_range function in order to check that total calculation is working fine with different situation.

## Instruction
I have use poetry for create the python project so it's compatible with python> 3.7
To execute the code it's necessary to have python installed.
By default the system considerate the file schedule.txt if there isn't any argument.

### Execute with Poetry:
- Install poetry for python https://python-poetry.org/docs/master/ 
- The in the terminal of the project directory run "poetry shell" and "poetry install"
- For see code help run "poetry run main --help"
- For execute the code run "poetry run main --file name_of_file.txt"
- For execute test run "poetry run pytest"