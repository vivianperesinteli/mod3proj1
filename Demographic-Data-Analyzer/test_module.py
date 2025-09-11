import unittest
import demographic_data_analyzer

class DemographicAnalyzerTestCase(unittest.TestCase):
    def setUp(self):
        self.data = demographic_data_analyzer.calculate_demographic_data(print_data=False)

    def test_race_count(self):
        actual = self.data['race_count']
        expected = [27816, 3124, 1039, 311, 271]
        self.assertAlmostEqual(actual.tolist(), expected, msg="Expected race count values to be [27816, 3124, 1039, 311, 271]")

    def test_average_age_men(self):
        actual = self.data['average_age_men']
        expected = 39.4
        self.assertAlmostEqual(actual, expected, msg="Expected average age of men to be 39.4")

    # ... (and so on for all other tests)
