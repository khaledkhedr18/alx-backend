#!/usr/bin/python3
'''Task 0's Module.'''

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    A basic caching system that stores data in a dictionary.
    """

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()

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

    def get(self, key):
        """
        Retrieves the value associated with the given key from the cache.

        Parameters:
            key (Any): The key to retrieve the value for.

        Returns:
            Any: The value associated with the given key,
            or None if the key is None or not found in the cache.
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
