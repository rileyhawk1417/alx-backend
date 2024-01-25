#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


def index_range(page, page_size):
    """The function returns a tuple.
    Of the page and page size(number of pages)
    """
    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size
    page_range = (start_idx, end_idx)
    return page_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Get results from indexed dataset
        """

        data = self.indexed_dataset()
        assert index is not None and isinstance(
            index, int) and index >= 0 and index <= max(data.keys())
        idx = index if index else 0
        raw_data = []
        next_index = None
        item_count = 0
        for _index, item in data.items():
            if _index >= idx and item_count < page_size:
                raw_data.append(item)
                item_count += 1
                continue
            if item_count == page_size:
                next_index = _index
                break
        processed = {
            'index': index,
            'data': raw_data,
            'page_size': len(raw_data),
            'next_index': next_index,
        }
        return processed
