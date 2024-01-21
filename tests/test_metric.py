import unittest
import logging
from src.ir_metric.metric import average_precision_at_k, precision_at_k, recall_at_k


class TestMetric(unittest.TestCase):
    def test_average_precision_basic(self):
        ground_truth = [1, 3, 5]
        predicted = [1, 2, 3, 4, 5]
        self.assertAlmostEqual(
            average_precision_at_k(ground_truth, predicted), 0.756
        )

    def test_average_precision_empty_predicted(self):
        ground_truth = [1, 3, 5]
        predicted = []
        self.assertEqual(average_precision_at_k(ground_truth, predicted), 0)

    def test_average_precision_empty_ground_truth(self):
        ground_truth = []
        predicted = [1, 2, 3, 4, 5]
        self.assertEqual(average_precision_at_k(ground_truth, predicted), 0)

    def test_average_precision_k_greater_than_predicted(self):
        ground_truth = [1, 3, 5]
        predicted = [1, 5, 3]
        self.assertAlmostEqual(average_precision_at_k(ground_truth, predicted, k=5), 1)

    def test_average_precision_k_is_zero(self):
        ground_truth = [1, 3, 5]
        predicted = [1, 2, 3, 4, 5]
        self.assertEqual(average_precision_at_k(ground_truth, predicted, k=0), 0)

    def test_average_precision_invalid_ground_truth(self):
        ground_truth = "not a list"
        predicted = [1, 2, 3, 4, 5]
        with self.assertRaises(ValueError):
            average_precision_at_k(ground_truth, predicted)

    def test_average_precision_invalid_predicted(self):
        ground_truth = [1, 3, 5]
        predicted = "not a list"
        with self.assertRaises(ValueError):
            average_precision_at_k(ground_truth, predicted)

    def test_average_precision_invalid_k(self):
        ground_truth = [1, 3, 5]
        predicted = [1, 2, 3, 4, 5]
        with self.assertRaises(ValueError):
            average_precision_at_k(ground_truth, predicted, k="not an int")


    def test_recall_at_k_basic(self):
        ground_truth = ["2", "4", "5", "7"]
        predicted = ["1", "2", "3", "4", "5", "6", "7", "8"]
        recall_value = [(1,0.0),(2,0.25),(3,0.25),(4,0.5),(5,0.75),(6,0.75),(7,1.0),(8,1.0)]
        for k, recall_val in recall_value:
            self.assertEqual(recall_at_k(ground_truth=ground_truth, predicted=predicted, k=k), recall_val)

    def test_precision_at_k_basic(self):
        ground_truth = ["2", "4", "5", "7"]
        predicted = ["1", "2", "3", "4", "5", "6", "7", "8"]
        precision_value = [(1,0),(2,0.5),(3,0.333),(4,0.5)]
        for k, precision_val in precision_value:
            self.assertEqual(precision_at_k(ground_truth=ground_truth, predicted=predicted, k=k),precision_val)

# Run the tests
if __name__ == "__main__":
    unittest.main()
