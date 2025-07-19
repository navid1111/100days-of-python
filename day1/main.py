# Datatypes 

# ==================
# Strings
# ==================
"Hello"
# We know string is a array of characters so we can pull out each of the characters individually
print("Hello"[0])
# output -> H 
# This way of pulling out a character from a string is called subscripting
print("Hello"[len("Hello")-1])

# ==================
# Integer
# ==================
print(124+345)

# ==================
# Float
# ==================
3.1416

# ==================
# Boolean 
# ==================
True
False

# If we give a number instead of a stirng iside the len function it will give us an error
# if we use print(len("hello")) we will see the numeber of characters in hello which is 5 but if we use len(2345) this will give us a TypeError TypeError: object of type 'int' has no len()
# Today we will learn a whole lot more about different datatyeps including string,integer,float and 
# imagine a machine that converts potatoes into chips . But if you give rocks inside the machine instead of potatoes that will give u a similar error 

num_char = len(input("What is your name?"))
# print("Your name has "+num_char+" characters.")
# This code will give us a type error
#Which says we cant concatinate an integer with a string
print(type(num_char))

# type conversion
new_num_char=str(num_char)
print("Your name has "+new_num_char+" characters.")

a=124
type(a)
a=float(a)
print(type(a))