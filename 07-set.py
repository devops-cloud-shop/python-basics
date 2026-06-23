s1 = set()
sample = {'s', 'd', 'f', 'd'}
print(sample)

#set is an unordered collection
# sets remove duplicates and stores unique values

# print(dir(set()))
"""
['add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
"""
s1 = { 1,35,4,3,28}
s2 = {1,25,4,3}
print(s1.difference(s2))