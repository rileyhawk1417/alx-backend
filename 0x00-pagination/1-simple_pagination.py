#!/usr/bin/env python3
"""
Pagination Module
"""

import csv
from typing import List


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

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get page gets the specified page and content
        page: int (default=1)
        page_size: int (default=10)
        """

        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()
        if start > len(data):
            return []
        indexedData = data[start:end]
        return indexedData
