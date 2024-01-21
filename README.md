# ir_metrics

## Overview

ir_metrics is a Python package designed to facilitate information retrieval (IR) metric calculations. It provides a simple and convenient way to compute various metrics commonly used in IR evaluation.

## Installation

Install the package using pip:

```
pip install ir_metric
```

## Quick Start

To use ir_metrics, import the metric module and call the desired metric function. Here's a quick example of computing the average precision:

python
from ir_metric import metric

# Example data
actual_ranking = [1, 2, 3]
predicted_ranking = [5, 3, 1]

# Compute average precision at k=2
result = metric.average_precision(actual_ranking, predicted_ranking, k=2)

print(result)  # Output: 0.25


## Available Metrics

Currently, ir_metrics supports the following metrics:

- Average Precision (average_precision)
- Precision at k (precision_at_k)
- Recall at k (recall_at_k)
- F1 Score at k (f1_score_at_k)


## Contributions

Contributions and bug reports are welcome! Feel free to open issues or submit pull requests on the GitHub repository: [https://github.com/harshkumarchourasia/ir_metric]

## License

This project is licensed under the MIT License.
