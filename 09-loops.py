# for, while
# continue, break 

value = 0

# #break
# while value < 10:
#     if value == 5:
#         break
   
#     value = value + 1
#     print(value)

#continue
# while value < 10:
#     if value == 5:
#         value = value + 1 #Incrementing is important
#         continue
#     value = value + 1
#     print(value)

#for
sample = [ "server_1", "server_2", "server_3", "server_4", "server_5" ]

for ele in sample:
    print (ele)

# ele = iterator
# sample = iterable

#ramge, enumerator

print (range(5))


#to access elements of the list we need type casting
print (list(range(5)))

#to access the elements in the list

for ele in (range(len(sample))):
    print (sample[ele])