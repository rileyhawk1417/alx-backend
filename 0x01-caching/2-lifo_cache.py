#!/usr/bin/env python3
"""Class that implements LIFO cache strategy"""
BaseCache = __import__('base_caching').BaseCaching


class LIFOCache(BaseCache):
    """LIFO Cache"""

    def __init__(self) -> None:
        super().__init__()
        self.max_items = BaseCache.MAX_ITEMS
        self.size = 0
        self.last_entry = None

    def put(self, key, item):
        """
        Add key as the dictionary key and item as the value for the key
        Remove the last value if max entries are reached
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
                self.last_entry = key
                return
            if self.size > self.max_items:
                self.cache_data.pop(self.last_entry)
                print(f"DISCARD: {self.last_entry}")
            self.cache_data[key] = item
            self.last_entry = key
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
