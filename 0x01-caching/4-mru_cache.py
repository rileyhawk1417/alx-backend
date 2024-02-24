#!/usr/bin/env python3
"""Class that implements MRU cache strategy"""
from collections import OrderedDict
BaseCache = __import__('base_caching').BaseCaching


class MRUCache(BaseCache):
    """MRU Cache
    Most Recently Used cache strategy.
    """

    def __init__(self) -> None:
        """Init the cache"""
        super().__init__()
        self.max_items = BaseCache.MAX_ITEMS
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        If not in cache add key.
        If Cache limit reached pop MRU then add.
        Args:
            key: The key to associate the value
            item: The value to associate the key
        Returns:
            Return None
        """
        if key and item:
            if key not in self.cache_data:
                if len(self.cache_data) + 1 > self.max_items:
                    mru_key, _ = self.cache_data.popitem(False)
                    print("DISCARD:", mru_key)
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
        if key and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
