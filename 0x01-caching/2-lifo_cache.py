#!/usr/bin/env python3
'''Task 2's Module.'''


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.cache_data = {}
        self.keys_order = []

    def put(self, key, item):
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.keys_order.remove(key)

        self.cache_data[key] = item
        self.keys_order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_key = self.keys_order.pop()
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}")

    def get(self, key):
        return self.cache_data[key]
