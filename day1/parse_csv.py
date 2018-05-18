import csv

'''
Write a program to parase a csv file (s) and obtain the item with min score difference. 

Problem
Problem
Football: The football.csv file contains the results from the English Premier League. The columns labeled ‘Goals’ and 
‘Goals Allowed’ contain the total number of goals scored for and against each team in that season (so Arsenal scored 
79 goals against opponents, and had 36 goals scored against them). Write a program to read the file, then print the 
name of the team with the smallest difference in ‘for’ and ‘against’ goals.

Weather: In weather.csv you’ll find daily weather data. Write a program to read the file, then output the day number 
(column one) with the smallest temperature spread (the maximum temperature is the second column, the minimum the 
third column).
See if you can write the same program to solve both questions.
'''


def read_csv(file_name):
    with open(file_name, 'r') as f:
        return [row for row in csv.reader(f)]


def get_min_score_difference(parsed_data):
    parsed_data.pop(0)
    goals_scored = [x[5] for x in parsed_data]
    goals_allowed = [x[6] for x in parsed_data]

    print(goals_allowed)
    print(goals_scored)
    values = [int(x) - int(y) for x, y in zip(goals_scored, goals_allowed)]
    print(values)
    return values.index(min(values))


def get_team(index, parsed_data):
    teams = [x[0] for x in parsed_data]
    return teams[index]
