l = []
l1 = list()

server_1 = "172.10.33.25"
server_2 = "172.10.33.26"

servers = [ "172.10.33.25" , "172.10.33.26" , True, 123, 123.45, False, 456 ]
print(type(servers), servers)


#Python is ZERO index based
server_1 = servers[0]
print("server_1 is:", server_1)

#Slicing - has (startindex:endindex, stepsize) end index is not inclusive 
slicing_server = servers[0:2]
print(slicing_server)

# suppose you want to fetch servers in odd index like 1st element, 3rd element, 5th element from the list
#here we make use of step size - by default step size value is 1

slicing_server = servers[1:6:2]
print(slicing_server)

slicing_server = servers[0:7:2] #even
print(slicing_server)

#Negative indexing
slicing_server = servers[-1:-6:-1] 
print(slicing_server)
print("Length of list:", len(slicing_server))

print("Length of list:", len(servers))

# List is a mutable datatype
# Mutable: Once defined, can change at any time E.g. List, dictonaries
# Immutable: Once defined, can't be changed E.g. Tuple, sets

servers[-2] = "Ansible"
print("After_Modification:", servers)


# To know the operations performed by a specific datatype ex-list - use dir(variable/datatype)
# print("list_of_operations:",dir(servers))

"""
'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

"""

#append - lists the object to the end of the list
servers = [ "172.10.33.25" , "172.10.33.26" , True, 123, 123.45, False, 456 ]
servers.append(True)
print("after_append:", servers)

#you can add/append list in a list
servers.append(["a", "b"])
print("after_append_list:", servers)

#Multi indexing

print(servers[-1][0]) #when u want to fetch an element from the list in a list


# extend- it extends list by appending the elements of the iterable - ex- if string is given "extra", it appends as "e"
#,"x", "t", "r", "a" - if list is given ["c", "d"] - it appends as "c" , "d" at the end of the list.

#bool object throws an error - can't extend
servers.extend(["c","d"]) 
print("after_modify_extend:", servers)

#index

print("modify index:", servers.index(False))

#insert - need to specify index of the value to be added- so that it inserts the value at the specified index
print("before_modify:", servers)
servers.insert(5,"554.45.43.2")
print("after_insert:", servers)

#remove

servers.remove(True)
print("after_remove:", servers)

#reverse
servers.reverse()
print(servers)

servers_actual = servers[::-1] # to list the servers before reverse operation had applied
print("original_list:", servers_actual)

#sort - Inplace operation -means it results "None", the list is updated inplace
#sorted - returns a new list
servers = [ 1,43,6,7,4,9,0,3,5 ]
servers.sort()
print("sorting:", servers)

servers_1 = sorted(servers)
print(servers, servers_1)





























""" # print("Before modify:", servers)
servers[-3] = 1234 # Inplace operation
# print("After modification:", servers)

# print("List of operations:", dir(servers))

"""
['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
"""
servers = ["172.10.33.25", "172.10.33.26", True, 123, 1234.56, 1234.567, True]
print("Before:", servers)
servers.append(False)
print("After:", servers)
servers.append(["a", "b"])
print("After append:", servers, len(servers))
# Multi indexing
# print(servers[-1][0])
servers.extend(["c", "d"])
print("After extend:", servers, len(servers))
print(servers.index(True))
servers.insert(0, 12)
print(servers)
servers.remove(True)
print(servers)
servers.reverse()
print(servers)
servers = servers[::-1]
print(servers)

servers = [1, 5, 7, 9, 2, 4, 3]
# servers.sort()
servers_1 = sorted(servers)
print(servers, servers_1)

servers = ["172.10.33.25", "172.10.33.26", True, 123, 1234.56, 1234.567, True]
servers_1 = servers.copy()
servers_1.remove(123)
print(servers, servers_1)

# """
# 1. Reverse a list
# 2. Sort vs sorted
# 3. Integer division vs floor division
# 4. Shallow copy (inplace operation)
# 5. Multi indexing
# 6. append vs extend
# 7. Mutable vs immutable
# 8. dir()
# """

# servers_1.remove(123456) # it throws an error when the element is not present in the list """ """