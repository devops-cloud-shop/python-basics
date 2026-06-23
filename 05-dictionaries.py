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

print(sample.keys(), sample.values(), sample.items())

#Type Casting
# sample = [('b','e'), (1,2), 2 ,3] # this list cant be converted to dict - The list should be in a sequence to convert to a dict
sample = [ (('a','b'), 3), (('g','h'),'f')] # This can be converted as the list has elements following a sequence or organized to convert to dict.
print(dict(sample))

