#!/usr/bin/env python3
"""Class that implements LRU cache strategy"""
from collections import OrderedDict
BaseCache = __import__('base_caching').BaseCaching


class LRUCache(BaseCache):
    """LRU Cache"""

    def __init__(self) -> None:
        """Init the cache"""
        super().__init__()
        self.max_items = BaseCache.MAX_ITEMS
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Add key in cache if not present.
        If max cache items reached remove LRU then add.
        Args:
            key: The key to associate the value
            item: The value to associate the key
        Returns:
            Return None
        """
        if key and item:
            if key not in self.cache_data:
                if len(self.cache_data) + 1 > self.max_items:
                    lru_key, _ = self.cache_data.popitem(True)
                    print('DISCARD:', lru_key)
                self.cache_data[key] = item
                self.cache_data.move_to_end(key, last=False)
            else:
                self.cache_data[key] = item
        return

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
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
