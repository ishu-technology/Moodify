# OOPS IN PYTHON

class Employee:
    def __init__(self):
        self.name= input('enter name:')
        # self.department= input('enter department:')
        self.salary=(input('enter salary: $'))
    def display(self):
        print("name is", self.name )
    #     print("department is", self.department)
        print("salary is", self.salary)

    
n= int(input("Enter number of employees:"))
Employees=[]
for i in range(1,n+1):
    e1=Employee()
    Employees.append(e1)

for e in Employees:
    e.display()

highest_paid= max(Employees,key= lambda x:x.salary)
lowest_paid= min(Employees, key=lambda x:x.salary)

print("highest paid:") 
highest_paid.display()

print("lowest paid:")
lowest_paid.display()


#     def more_salary(e1,e2,e3):

#        if e1.salary> e2.salary and e1.salary> e3.salary:
#          print("salary of e1 is more than the 2 ")

#        elif e2.salary> e1.salary and e2.salary> e3.salary:
#          print("salary of e2 is more than the 2")

#        elif e3.salary> e1.salary and e3.salary> e2.salary:
#          print("salary of e3 is more than the 2")

#        else:
#          print("salary is same")    

# e1= Employee() 
# e2= Employee()               
# e3= Employee()  

# e1.display()
# e2.display()
# e3.display()
# e1.more_salary(e2,e3)
