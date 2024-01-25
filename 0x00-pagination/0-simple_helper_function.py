#!/usr/bin/env python3
"""Simple module that returns number of pages and index"""


def index_range(page, page_size):
    """The function returns a tuple.
    Of the page and page size(number of pages)
    """
    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size
    page_range = (start_idx, end_idx)
    return page_range
