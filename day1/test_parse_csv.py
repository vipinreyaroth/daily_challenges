'''
This is the test driven approach.
This is a test script to test the parsing/reading of the csv file.
In this iteration, we will test if the program is able to parse the 'football.csv' file correctly.
The tests will check the header, and the some data to test if the data is read correctly.
'''

from parse_csv import ParseCsv
import unittest

class ParseCSVTest(unittest.TestCase):
    def setUp(self):
        self.football_data = 'football.csv'
        self.weather_data = 'weather.csv'
        self.football = ParseCsv(self.football_data)
        self.weather = ParseCsv(self.weather_data)

        self.parsed_data_football = [['Team', 'Games', 'Wins', 'Losses', 'Draws', 'Goals', 'Goals Allowed', 'Points'],
               ['Arsenal', '38', '26', '9', '3', '79', '36', '87'],
               ['Liverpool', '38', '24', '8', '6', '67', '30', '80']]
        self.parsed_data_weather = [['Day', 'MxT', 'MnT', 'AvT', 'AvDP', '1HrP TPcpn', 'PDir', 'AvSp', 'Dir', 'MxS',
                                    'SkyC', 'MxR', 'Mn', 'R AvSLP'],
        ['1', '88', '59', '74', '53.8', '0', '280', '9.6', '270', '17', '1.6', '93', '23', '1004.5'],
        ['2', '79', '63', '71', '46.5', '0', '330', '8.7', '340', '23', '3.3', '70', '28', '1004.5']]

    def test_csv_read_data_headers(self):
        self.assertEqual(self.football.read_data()[0], ['Team', 'Games', 'Wins', 'Losses', 'Draws', 'Goals',
                                                       'Goals Allowed', 'Points'])
        self.assertEqual(self.weather.read_data()[0], ['Day', 'MxT', 'MnT', 'AvT', 'AvDP', '1HrP TPcpn', 'PDir',
                                                        'AvSp', 'Dir', 'MxS', 'SkyC', 'MxR', 'Mn', 'R AvSLP'])

    def test_read_data_team_name(self):
        self.assertEqual(self.football.read_data()[1][0], 'Arsenal')

    def test_read_data_day(self):
        self.assertEqual(self.weather.read_data()[1][0], '1')

    def test_read_data_points(self):
        self.assertEqual(self.football.read_data()[1][7], '87')
        self.assertEqual(self.weather.read_data()[1][1], '88')

    def test_get_min_score_difference(self):
        self.assertEqual(self.football.get_min_score_difference(self.parsed_data_football, 5, 6), 1)
        self.assertEqual(self.weather.get_min_score_difference(self.parsed_data_weather, 2, 3), 0)

    def test_get_team(self):
        self.assertEqual(self.football.get_team(self.football.get_min_score_difference(self.parsed_data_football, 5, 6),
                                                self.parsed_data_football), 'Liverpool')

    def test_get_day(self):
        self.assertEqual(self.weather.get_day(self.weather.get_min_score_difference(self.parsed_data_weather, 2, 3),
                                              self.parsed_data_weather), '1')
