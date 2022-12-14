from utils.api import get_input

input_str = get_input(2)

# WRITE YOUR SOLUTION HERE

def get_neat_list(input):
    sections = input.split('\n\n')

    split_string = []
    for sub in sections:
        split_string.append(sub.split('\n'))

    return(split_string[0])

sorted_input = get_neat_list(input_str)

total_score = 0
key = {'A':'rock', 'B':'paper', 'C':'scissors', 'X':'rock', 'Y':'paper', 'Z':'scissors',
       'rock':['scissors', 1], 'paper':['rock', 2], 'scissors':['paper', 3]}
"""
0 = Strengths
1 = Score for item
"""
scores = [0, 3, 6]
for round in sorted_input:
    round = round.split()
    opponent = key[round[0]]
    player = key[round[1]]
    if opponent == player:
        total_score = total_score + 3 + key[player][1]
    elif key[player][0] == opponent:
        total_score = total_score + 6 + key[player][1]
    elif key[opponent][0] == player:
        total_score = total_score + 0 + key[player][1]

print(total_score)

