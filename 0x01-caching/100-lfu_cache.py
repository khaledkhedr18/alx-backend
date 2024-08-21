#!/usr/bin/env python3
'''LFU Caching Module'''
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    '''
    LFUCache is a Least Frequently used caching system
    '''

    def __init__(self):
        '''Initialize.'''
        super().__init__()
        self.cache_data = {}
        self.use_count = {}

    def put(self, key, item):
        """
        Adds an item to the cache.

        Parameters:
            key (Any): The key to associate with the item.
            item (Any): The item to store in the cache.

        Returns:
            None
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if key in self.use_count:
            self.use_count[key] += 1
        else:
            self.use_count[key] = 1

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_four = list(self.use_count.keys())[:BaseCaching.MAX_ITEMS]
            lfu_key = min(first_four, key=lambda k: (self.use_count[k], k))
            del self.cache_data[lfu_key]
            del self.use_count[lfu_key]
            print(f"DISCARD: {lfu_key}")

    def get(self, key):
        """
        Retrieves a value from the cache by its key.

        Args:
            key (Any): The key associated with the desired value.

        Returns:
            Any: The cached value associated with the given key,
            or None if the key is None or not found in the cache.
        """
        if key is None or key not in self.cache_data:
            return None
        self.use_count[key] += 1
        return self.cache_data[key]
