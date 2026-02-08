# CODE1(How to print something)

print("hello world\n" * 10 )

# CODE2(Arithmetic operations) 

a=2
b=5
c=a+b
print(c) 

# CODE3(Taking input from user)

num1 = input("Enter a number:")
b= num1+5.6

print(b)
# Now, here will come an error, because i haven't defined the return datatype of number which is taken as input 
# So, the correct code will be-----


# CODE4(Defining return datatype)

num1 = float(input("Enter a number:"))
b=num1+5.6

print(b)

# CODE5(To calculate the area and circumference of the circle)

r= float(input("enter the radius:"))
area=float(3.14*r*r)

circumference= 2*float(3.14*r)
print("The area of circle is",area)
print("The circumference of circle is", circumference)