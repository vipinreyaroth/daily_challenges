'''
This is the test driven approach.
This is a test script to test the parsing/reading of the csv file.
In this iteration, we will test if the program is able to parse the 'football.csv' file correctly.
The tests will check the header, and the some data to test if the data is read correctly.
'''

from parse_csv import read_csv, get_min_score_difference, get_team

FILE_NAME = 'football.csv'
parsed_data = [['Team', 'Games', 'Wins', 'Losses', 'Draws', 'Goals', 'Goals Allowed', 'Points'],
               ['Arsenal', '38', '26', '9', '3', '79', '36', '87'],
               ['Liverpool', '38', '24', '8', '6', '67', '30', '80']]

def test_csv_read_data_headers():
    assert read_csv(FILE_NAME)[0] == ['Team', 'Games', 'Wins', 'Losses', 'Draws', 'Goals',
                                                  'Goals Allowed', 'Points']


def test_csv_read_data_team_name():
    assert read_csv(FILE_NAME)[1][0] == 'Arsenal'


def test_csv_read_data_points():
    assert read_csv(FILE_NAME)[1][7] == '87'


def test_get_min_score_difference():
    assert get_min_score_difference(parsed_data) == 1


def test_get_team():
    assert get_team(get_min_score_difference(parsed_data), parsed_data) == 'Liverpool'

