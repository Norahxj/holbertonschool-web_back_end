#!/usr/bin/env python3
"""This module provides deletion-resilient hypermedia pagination."""

import csv
from typing import Dict, List


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize the server with cached datasets set to None."""
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Return the cached dataset loaded from the CSV file."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Return the dataset indexed by sorting position, starting at 0."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }

        return self.__indexed_dataset

    def get_hyper_index(
        self,
        index: int = None,
        page_size: int = 10
    ) -> Dict:
        """Return a deletion-resilient page with pagination metadata."""
        indexed_data = self.indexed_dataset()

        if index is None:
            index = 0

        assert isinstance(index, int)
        assert isinstance(page_size, int) and page_size > 0
        assert index >= 0 and index <= max(indexed_data.keys())

        data = []
        next_index = index

        while len(data) < page_size and next_index <= max(indexed_data.keys()):
            if next_index in indexed_data:
                data.append(indexed_data[next_index])
            next_index += 1

        return {
            "index": index,
            "data": data,
            "page_size": len(data),
            "next_index": next_index,
        }
