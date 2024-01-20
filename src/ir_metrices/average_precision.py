from typing import List, Any, Optional


def average_precision(
    ground_truth: List[Any], predicted: List[Any], k: Optional[int] = None
):
    """
    Calculate the average precision (AP) at a given cut-off rank (k) for a single information retrieval query.

    Average precision computes the average of precision values at the points where each relevant document is retrieved. It is a measure that takes into account the order of the retrieved documents, with a focus on the ranking of relevant documents.

    Parameters:
    - ground_truth (list): A list of elements that are the "ground truth" (relevant documents/items).
    - predicted (list): A list of elements that are the predicted documents/items, ordered by relevance.
    - k (int, optional): The cut-off rank up to which the precision is calculated. If not specified, the length of the predicted list is used.

    Returns:
    - float: The average precision at the given cut-off rank k. If there are no relevant items in the top k predictions or the ground_truth is empty, returns 0.

    Examples:
    >>> ground_truth = [1, 3, 5]
    >>> predicted = [1, 2, 3, 4, 5]
    >>> average_precision(ground_truth, predicted)
    0.7555555555555555

    >>> average_precision(ground_truth, [], k=3)
    0

    Note:
    - The function assumes that the ground_truth and predicted lists do not contain duplicates.
    - Elements in the ground_truth and predicted lists can be of any hashable type.
    - If k is greater than the length of the predicted list, the function will use the length of the predicted list as k.
    - If the ground_truth list is empty, the function will return 0, as there are no relevant items to be retrieved.
    """

    # Validate that ground_truth and predicted are lists
    if not isinstance(ground_truth, list):
        raise ValueError("ground_truth must be a list.")
    if not isinstance(predicted, list):
        raise ValueError("predicted must be a list.")

    # Validate that k is a non-negative integer if provided, and handle the case where k is larger than the length of predicted
    if k is not None and (not isinstance(k, int) or k < 0):
        raise ValueError("k must be a non-negative integer.")

    k = len(predicted) if k is None else k
    if not len(ground_truth):
        return 0

    # Initialize necessary variables
    num_hits = 0
    sum_precisions = 0

    # Iterate over the predicted list up to the k-th element
    for i, p in enumerate(predicted[:k]):
        if p in ground_truth:
            num_hits += 1
            precision_at_i = num_hits / (i + 1)
            sum_precisions += precision_at_i

    # If there are no relevant items in the top k predictions, return 0
    if num_hits == 0:
        return 0

    # Calculate the final average precision
    ap_score = sum_precisions / min(len(ground_truth), k)
    return ap_score
