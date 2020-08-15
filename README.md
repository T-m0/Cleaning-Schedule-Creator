# Cleaning-Schedule-Creator

This script creates a simple cleaning schedule as a pandas dataframe, and writes it to a Microsoft Excel file.

## Prerequisites
The libraries numpy and pandas are required to create the schedule. To install them:

```
pip install numpy
```
and for pandas:
```
pip install pandas
```
## How to use
There are four variables that you can (and should) change: chores, names, max_width and schedule_length. Change these to fit your own household.  
Chores is a list of chores, with each chore being a string. These will become the column titles of the schedule.  
Names is a list of names, with each name being a string.  
Max_width is an integer, representing the maximum amount of columns that you want your cleaning schedule to be.  
Schedule_length is an integer, representing the amount of weeks you want the schedule to have.  

### A small request for you, the user
I'm very much still a beginner in programming and this is my first project. If I made any huge errors that someone working in python shouldn't make, or if you have a suggestion on how to improve the schedule: please let me know.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgements
Thanks to reddit user onmywaybackhome for pointing me towards a stackoverflow answer from Pacific-Stickler, which allowed me to cycle through the list of names.
