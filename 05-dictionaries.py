d = {}
d1 = dict()
#dictionaries are key-value pairs, also known as hashmaps

sample = { 'a':1 , 'b':2 }
print(sample['a'], sample.get('b'))

#dictionaries are mutable

sample['a'] = 10
print(sample['a']) # a value can be modified

# Value can be modified But Keys cannot be modified

#example
sample = {('a' , 'b'): 18, 'd' : 24}
print(type(sample), sample)

# print(dir(dict))
"""
['clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
"""
