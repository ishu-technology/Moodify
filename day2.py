# 1ST CODE
movie1=input( "Enter movie name:")
tickets1=int(input("Enter number of tickets:"))
price1=float(input("Enter price per ticket:"))
print("")

movie2=input("Enter movie name:")
tickets2=int(input("Enter number of tickets:"))
price2=float(input("Enter price per ticket:"))
print("")

movie3=input("Enter movie name:")
tickets3=int(input("Enter number of tickets:"))
price3=float(input("Enter price per ticket:"))
print("")

print("-----TICKET SUMMARY-------")
a= tickets1*price1
print(f"{movie1}-{tickets1} tickets x ${price1}={a}")
b=tickets2*price2
print(f"{movie1}-{tickets2} tickets x ${price2}={b}")
c=tickets3*price3
print(f"{movie3}-{tickets3} tickets x ${price3}={c}")

total=a+b+c
print(f"Total:{total}")


# # 2ND CODE(Number is even or odd)

num1=int(input("Enter a no.:"))
if num1%2==0:
    print("number is even")
else:
    print("number is odd")

# # 3RD CODE(Greater among 3 numbers)

num1=float(input("Enter a number:"))
num2=float(input("Enter a number:"))
num3=float(input("Enter a number:"))

if num1>num2 and num1>num3:
    print("num1 is greater than other 2 numbers")

elif num2>num1 and num2>num3:
    print("num2 is greater than other 2 numbers") 

elif num3>num1 and num3>num2:
    print("num3 is greater than other 2 numbers")

else:
    print("numbers are equal")

# # 4TH CODE(Print multiplication table of a no.)

num=int(input("Enter a no.:"))

for i in range(1,11):


     print(f"{num} x {i} = {num *i}")

     