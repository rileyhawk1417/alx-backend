#!/usr/bin/env python3

"""
This module inherits from BaseCaching
"""

BaseCache = __import__('base_caching').BaseCaching


class BasicCache(BaseCache):
    """Basic Cache Class"""

    def put(self, key, item):
        """
        Store key as the cache key in cache_data
        Then use item as the value for the key
        Args:
            key: The key to associate the value
            item: The value to associate the key
        Returns:
            Return the dictionary value if none, return None
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Find key in cache_data if found return value
        if not found return none
        Args:
            key: The key to search for
        Returns:
            Return the dictionary value if none, return None
        """
        if key and key in self.cache_data:
            return (self.cache_data[key])
        return None
