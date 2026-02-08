# FUNCTIONS
# 2 types : Built in and user defined functions

# function to add 2 numbers
# def add(a,b):
#     print(a+b)   
# add(4,5)
# add(6.7,8.3)

# 
# def add(a,b):
#     # print(a+b)
#     return(a+b)
# c=add(5,7) #for storing
# print(add(c,add(5.6,6))) #nested function call
# print('sum is:' , add(2.3,6.8))

# CODE1(to add numbers)

# def add(*numbers):
#     return sum(numbers)
# num1=(input('numbers u want to add:'))

# num_list=[]
# for x in num1.split():
#     num_list.append(float(x))

# print("Sum:" , add(*num_list))

#CODE2 (calculator function)
def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def mul(a,b):
    mul(a*b)
def div(a,b):
    div(a/b)




    


