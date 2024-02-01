#!/usr/bin/env python3
"""Class that implements MRU cache strategy"""
from collections import deque as queue
BaseCache = __import__('base_caching').BaseCaching


class MRUCache(BaseCache):
    """MRU Cache"""

    def __init__(self) -> None:
        super().__init__()
        self.max_items = BaseCache.MAX_ITEMS
        self.size = 0
        self.mru_queue = queue()

    def put(self, key, item):
        """
        Add key as the dictionary key and item as the value for the key
        Remove the least used value & key if max entries are reached
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
                """
                Remove current position for key 
                and add to the top of the queue
                """
                self.mru_queue.remove(key)
                self.mru_queue.append(key)
                return
            if self.size > self.max_items:
                prev = self.mru_queue.pop()
                self.cache_data.pop(prev)
                print(f"DISCARD: {prev}")
            self.cache_data[key] = item
            self.mru_queue.append(key)
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
            """
            Remove value at current position
            Move it to the top of the queue
            """
            self.mru_queue.remove(key)
            self.mru_queue.append(key)
            return (self.cache_data[key])
        return None
