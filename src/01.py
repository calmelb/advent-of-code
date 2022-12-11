from utils.api import get_input
import re
input_str = get_input(1)




# WRITE YOUR SOLUTION HERE

'''
This solves day 1 challenge for the advent of code 2022

The challenge involves calories, with below being an example list: 
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000


- The first Elf is carrying food with 1000, 2000, and 3000 Calories, a total of 6000 Calories.
- The second Elf is carrying one food item with 4000 Calories.
- The third Elf is carrying food with 5000 and 6000 Calories, a total of 11000 Calories.
- The fourth Elf is carrying food with 7000, 8000, and 9000 Calories, a total of 24000 Calories.
- The fifth Elf is carrying one food item with 10000 Calories.


Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?

# '''
def get_neat_list(input):
    sections = input.split('\n\n')

    split_string = []
    for sub in sections:
        split_string.append(sub.split('\n'))
    
    return(split_string)

def find_max(elf_list):
    elf_totals = []

    for elf in elf_list:
        elf_total = 0
        for cal in elf:
            elf_total = elf_total + int(cal)
        elf_totals.append(elf_total)

    return(max(elf_totals))


# MAIN PROGRAM
neat_list = get_neat_list(input_str)
largest_cal = find_max(neat_list)

print("Largest amount of calories in the group is: "+ str(largest_cal))