import unittest
import mean_var_std

class UnitTests(unittest.TestCase):
    def test_calculate_with_example_data(self):
        """ Tests calculation with the example dataset """
        actual = mean_var_std.calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
        expected = {
            'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
            'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
            'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
            'max': [[6, 7, 8], [2, 5, 8], 8],
            'min': [[0, 1, 2], [0, 3, 6], 0],
            'sum': [[9, 12, 15], [3, 12, 21], 36]
        }
        self.assertEqual(actual, expected)

    def test_calculate_with_different_data(self):
        """ Tests calculation with a different dataset """
        actual = mean_var_std.calculate([9, 1, 5, 3, 3, 3, 2, 9, 0])
        expected = {
            'mean': [[4.666666666666667, 4.333333333333333, 2.6666666666666665], [5.0, 3.0, 3.6666666666666665], 3.888888888888889],
            'variance': [[9.555555555555555, 11.555555555555557, 4.222222222222222], [10.666666666666666, 0.0, 14.888888888888891], 9.209876543209875],
            'standard deviation': [[3.0912061651652345, 3.39934634239519, 2.0548046676563256], [3.265986323710904, 0.0, 3.8586123009300755], 3.0347778408328137],
            'max': [[9, 9, 5], [9, 3, 9], 9],
            'min': [[2, 1, 0], [1, 3, 0], 0],
            'sum': [[14, 13, 8], [15, 9, 11], 35]
        }
        # We use assertEqual to compare dictionaries with floating point numbers
        self.assertEqual(actual, expected)

    def test_value_error_if_list_not_nine_numbers(self):
        """ Tests if a ValueError is raised if the list does not have 9 numbers """
        with self.assertRaisesRegex(ValueError, "List must contain nine numbers."):
            mean_var_std.calculate([1, 2, 3])

# Allows the tests to be run directly
if __name__ == "__main__":
    unittest.main()
