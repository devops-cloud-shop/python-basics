sample = "abd"
print(sample)

# sample[0] = 'h'
# print(sample)

#string doesnot support item assignment - means its a immutable datatype
# just like tuple and dict

""" print(dir('string'))
['capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'] """

#reverse a string
print(sample[::-1])

#Type casting

print(list(sample), tuple(sample))

sample_1 = "Hello, how are you doing"
print( sample_1.split(" "))

print("#".join(sample_1.split(" "))) # joining 2 string is concatenating them (adding/addition operation is performed internally "+")