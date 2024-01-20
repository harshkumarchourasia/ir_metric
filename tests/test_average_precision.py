import unittest

from src.ir_metrices.average_precision import average_precision

# Test cases for the average_precision function


class TestAveragePrecision(unittest.TestCase):
    def test_average_precision_basic(self):
        ground_truth = [1, 3, 5]
        predicted = [1, 2, 3, 4, 5]
        self.assertAlmostEqual(
            average_precision(ground_truth, predicted), 0.7555555555555555
        )

    def test_average_precision_empty_predicted(self):
        ground_truth = [1, 3, 5]
        predicted = []
        self.assertEqual(average_precision(ground_truth, predicted), 0)

    def test_average_precision_empty_ground_truth(self):
        ground_truth = []
        predicted = [1, 2, 3, 4, 5]
        self.assertEqual(average_precision(ground_truth, predicted), 0)

    def test_average_precision_k_greater_than_predicted(self):
        ground_truth = [1, 3, 5]
        predicted = [1, 5, 3]
        self.assertAlmostEqual(average_precision(ground_truth, predicted, k=5), 1)

    def test_average_precision_k_is_zero(self):
        ground_truth = [1, 3, 5]
        predicted = [1, 2, 3, 4, 5]
        self.assertEqual(average_precision(ground_truth, predicted, k=0), 0)

    def test_average_precision_invalid_ground_truth(self):
        ground_truth = "not a list"
        predicted = [1, 2, 3, 4, 5]
        with self.assertRaises(ValueError):
            average_precision(ground_truth, predicted)

    def test_average_precision_invalid_predicted(self):
        ground_truth = [1, 3, 5]
        predicted = "not a list"
        with self.assertRaises(ValueError):
            average_precision(ground_truth, predicted)

    def test_average_precision_invalid_k(self):
        ground_truth = [1, 3, 5]
        predicted = [1, 2, 3, 4, 5]
        with self.assertRaises(ValueError):
            average_precision(ground_truth, predicted, k="not an int")


# Run the tests
if __name__ == "__main__":
    unittest.main()
