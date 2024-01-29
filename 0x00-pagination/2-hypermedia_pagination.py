#!/usr/bin/env python3

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
        res = index_range(page, page_size)
        data = self.dataset()
        indexedData = data[res[0]:res[1]]
        return indexedData

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Get hyper following design of `HATEOAS`
        page: int (default=1)
        page_size: int (default=10)
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset())/page_size)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None
        processed = {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
        return processed
