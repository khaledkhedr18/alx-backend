#!/usr/bin/env python3
'''Task 3 Module'''

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    '''
    MRUCache is a most recently used caching system
    '''

    def __init__(self):
        """
        Initializes a new instance of the LRUCache class.
        """
        super().__init__()
        self.cache_data = {}
        self.mru_List = []

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
        if key in self.cache_data:
            self.mru_List.remove(key)

        self.mru_List.append(key)
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            mru_key = self.mru_List.pop(BaseCaching.MAX_ITEMS - 1)
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}")

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

        if key in self.cache_data:
            self.mru_List.remove(key)

        self.mru_List.append(key)
        return self.cache_data[key]
