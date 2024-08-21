#!/usr/bin/python3
""" 100-main """
LFUCache = __import__('100-lfu_cache').LFUCache

my_cache = LFUCache()
my_cache.put("A", "Hello") # 1
my_cache.put("B", "World") # 1
my_cache.put("C", "Holberton") # 1
my_cache.put("D", "School") # 1
my_cache.print_cache()
print(my_cache.get("B")) # B = 2
my_cache.put("E", "Battery") # E = 1, remove A
my_cache.print_cache() # B: 2, C: 1, D: 1, E: 1
my_cache.put("C", "Street") # B: 2, C: 2, D: 1, E: 1
my_cache.print_cache()
print(my_cache.get("A")) #None
print(my_cache.get("B")) # B: 3, C: 2, D: 1, E: 1
print(my_cache.get("C")) # B: 3, C: 3, D: 1, E: 1
my_cache.put("F", "Mission") # B: 3, C: 3, E: 1, F: 1
my_cache.print_cache()
my_cache.put("G", "San Francisco")# B: 3, C: 3, F: 1, G: 1
my_cache.print_cache()
my_cache.put("H", "H") # B: 3, C: 3, G: 1, H: 1
my_cache.print_cache()
my_cache.put("I", "I") # B: 3, C: 3, H: 1, I: 1
my_cache.print_cache()
print(my_cache.get("I")) # B: 3, C: 3, H: 1, I: 2
print(my_cache.get("H")) # B: 3, C: 3, H: 2, I: 2
print(my_cache.get("I"))# B: 3, C: 3, H: 2, I: 3
print(my_cache.get("H"))# B: 3, C: 3, H: 3, I: 3
print(my_cache.get("I"))# B: 3, C: 3, H: 3, I: 4
print(my_cache.get("H"))# B: 3, C: 3, H: 4, I: 4
my_cache.put("J", "J")
my_cache.print_cache()
my_cache.put("K", "K")
my_cache.print_cache()
my_cache.put("L", "L")
my_cache.print_cache()
my_cache.put("M", "M")
my_cache.print_cache()
