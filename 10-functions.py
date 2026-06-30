# def func_name():
#     print ("Hello")
# print (func_name())

def mult(a,b):
    return a * b
result = mult(3,4)
print (result)

#def funt doesn't need specific datatype to assign it to the variable
#even when you mention a:int , b:float - it doesnot restrict user from giving other datatypes
# so not recommended to specify datatype
# we use args for positional arguments and kwargs for keyword arguments

#     # *args -> pass any no: of position arguments
#     # **kwargs -> pass any no: keyword arguments

# a=4, b=5 are keyword arguments, as they contains keys and values
# '3.0', 3 are called as positional arguments

def mult(a,b, *args, **kwargs):
    print(f"a:{a}, b:{b}, args:{args}, kwargs:{kwargs}") # For readability and to make others/users know which variable has got which values
    return (a + b)
result = mult(3, 7 , 5, c=6, d=9 )
print(result)


def calc(a, b, operation):
    if operation == "add":
        return a + b
    if operation == "sub":
        return a - b
    if operation == "mult":
        return a * b
    if operation == "div":
        return a % b


#example  
# def sample(var):
#     return int(var)+1
# values =  list(map(sample,  input("Enter 2 number:").split()))

a, b =  list(map(int,  input("Enter 2 number:").split()))
operation = input("Enter operation to perform (add, sub, mult, div): ")
result = calc(a, b, operation)
print(result)
    
# a, b = tuple(map(int, input("Enter 2 numbers: ").split()))
# operation = input("Enter operation to perform (add, sub, mult, div): ")
# res = calc(a, b, operation)
# print(res)