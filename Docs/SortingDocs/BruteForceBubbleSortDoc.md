# Sorting - Brute Force Bubble Sort

## Table of Contents
[Overview](#Overview)

[The Code - Explained](#the-code-explained)

### Overview
This program resembles the Brute Force Bubble Sort. It uses the ideas presented in the psuedocode and translates it to real code/

### The Code - Explained
The first function that is created is known as swapPos(). This function takes in three arguments: lstS, pos1, pos2. lstS is a list, pos1 is one of the position that needs to be swapped from given list, and pos2 is the other position. Essentially, swapPos swaps the values in the given positions from the given list.
The second funtion is checkList(). This function takes in one argument: lst. lst is a list. checkList() checks if the given list is in correct ascending order and returns either True or False.
The third function is bruteBubble(). It takes in one argument: lst. lst is once again a list. First it creates isWorking a boolean variable which is initialized to False. Then it runs a While loop until isWorking becomes True. It then runs a For loop which will determine if the value before it is bigger or smaller than so it can determine where to place it. After the for loop is complete we used checkList() to determine if the list has truly been sorted.
