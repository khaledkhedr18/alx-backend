#!/usr/bin/python3
'''Task 1's Module.'''

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''FIFO caching system'''

    def __init__(self):
        '''Initiliaze'''
        super().__init__()
        self.cache_data = {}
        self.keys_order = []

    def put(self, key, item):
        """
        Add an item in the cache

        Parameters:
            key (Any): The key to associate with the item.
            item (Any): The item to store in the cache.
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.keys_order.remove(key)

        self.cache_data[key] = item
        self.keys_order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            oldest_key = self.keys_order.pop(0)
            del self.cache_data[oldest_key]
            print("DISCARD: {}".format(oldest_key))

    def get(self, key):
        """
        Retrieves a value from the cache by its key.

        Args:
            key (Any): The key associated with the desired value.

        Returns:
            Any: The cached value associated with the given key,
            or None if the key is None or not found in the cache.
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
