t = ()
t1 = tuple()

servers = ("172.10.33.25" , "172.10.33.26" , True, 123, 123.45, False, 456)
print(type(servers), servers)

#tuple is immutable -means once defined can't be modified
print(servers[0])

# servers[-1] = 44 #CANNOT modify the index -1 element to 44 - it throws an error
# print("after_modify:", servers)

slicing_servers = servers[1:5]
slicing_servers = servers[-2]
print("after_modify:", slicing_servers)

print(servers[0:6:2])

# tuple is useful when you have decided to not make any changes or modifications to any element/value
# ex- environments - dev,qa,prod

env_list = ("DEV", "QA", "PREPROD", "PROD")

# print(dir(tuple))
"""
['count', 'index']

"""

sample = (1,3,3,5,6,7,3,3,41)
print(sample.count(3), sample.count(33))

print(sample.index(7))

#Type casting - Datatype conversion

#converting tuple to list
env = ("DEV", "QA", "PREPROD", "PROD")

env_1 = list(env)
print(type(env_1), env_1)

# converting list to tuple
env_t = tuple(env_1)
print(type(env_t), env_t)




