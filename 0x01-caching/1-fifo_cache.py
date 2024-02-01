#!/usr/bin/env python3
"""Class that implements FIFO cache strategy"""
from collections import deque as queue
BaseCache = __import__('base_caching').BaseCaching


class FIFOCache(BaseCache):
    """FIFO Cache"""

    def __init__(self) -> None:
        super().__init__()
        self.fifo_queue = queue()
        self.max_items = BaseCache.MAX_ITEMS
        self.size = 0

    def put(self, key, item):
        """
        Add key as the dictionary key and item as the value for the key
        Remove the first value if max entries are reached
        Args: 
            key: The key to associate the value
            item: The value to associate the key
        Returns:
            Return None
        """
        if key and item:
            self.size += 1
            if key in self.cache_data:
                self.cache_data[key] = item
                return
            if self.size > self.max_items:
                prev = self.fifo_queue.popleft()
                self.cache_data.pop(prev)
                print(f"DISCARD: {prev}")
            self.cache_data[key] = item
            self.fifo_queue.append(key)
        return None

    def get(self, key):
        """
        Return the value linked with the key
        If not return None
        Args: 
            key: The key to associate the value
            item: The value to associate the key
        Returns:
            Return None
        """
        if key and key in self.cache_data:
            return (self.cache_data[key])
        return None
