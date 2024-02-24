#!/usr/bin/env python3
"""
Least Frequently Used Caching Module
"""
from collections import OrderedDict

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    Least Frequently Used will remove items
    from cache that are not used often, when limit is reached.
    Then add new items.
    LFU keys will be placed in a dictionary.
    """

    def __init__(self):
        """Initializes the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.freq_keys = []

    def __reorder_items(self, mru):
        """
        Reorder items in cache based on most recently used.
        Args:
            mru_key: most recently used item key
        """
        max_pos = []
        mru_freq = 0
        mru_pos = 0
        entry_pos = 0
        for i, key_freq in enumerate(self.freq_keys):
            if key_freq[0] == mru:
                mru_freq = key_freq[1] + 1
                mru_pos = i
                break
            elif len(max_pos) == 0:
                max_pos.append(i)
            elif key_freq[1] < self.freq_keys[max_pos[-1]][1]:
                max_pos.append(i)
        max_pos.reverse()
        for pos in max_pos:
            if self.freq_keys[pos][1] > mru_freq:
                break
            entry_pos = pos
        self.freq_keys.pop(mru_pos)
        self.freq_keys.insert(entry_pos, [mru, mru_freq])

    def put(self, key, item):
        """
        Add an item to cache.
        Args:
            key: the key of the item
            item: the value to use
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lfu_key, _ = self.freq_keys[-1]
                self.cache_data.pop(lfu_key)
                self.freq_keys.pop()
                print("DISCARD:", lfu_key)
            self.cache_data[key] = item
            ins_index = len(self.freq_keys)
            for i, key_freq in enumerate(self.freq_keys):
                if key_freq[1] == 0:
                    ins_index = i
                    break
            self.freq_keys.insert(ins_index, [key, 0])
        else:
            self.cache_data[key] = item
            self.__reorder_items(key)

    def get(self, key):
        """Get item value by key
        Args:
            key: specified key for value
        """
        if key is not None and key in self.cache_data:
            self.__reorder_items(key)
        return self.cache_data.get(key, None)
