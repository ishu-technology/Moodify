# CODE1(To print sum of first 10 natural numbers)
# sum=0
# for i in range(1,11):
#     sum = sum +i
# print("sum is" , sum)    


# # CODE2(Take input from users of any 10 numbers , calculate their sum and average)

# sum =0
# for num in range(1,11):
#     num =int(input("Enter number:"))
#     sum= sum+num

# print("sum is" , sum ) 
# print("average is" , sum/10)  


# # NEXT TOPIC:- COLLECTIONS
# # TYPES => 1)Lists
# #          2)Tuple
# #          3)Set
# #          4)Dictionary

 
# # CODE3(DIFFERENT FUNCTIONS IN LIST) 

# course=["html", "css", "java", "python", "react" , "c"]
# # to add object at the end of the list
# course.append("javascript")   
# to insert object at any index
# course.insert(4,"c++")
# # to remove object with the name
# course.remove("java")
# # to delete an object by giving index
# del course[2]
# # to pop out the object from the end
# course.pop()
# # to update the list
# course[1]="css(cascading style sheets)"
# for i in course:
# print(course)


#CODE4(Homework)

course=[]

while True:
    print(f"enter your choice: 1) add , 2) delete , 3) exit")
    choice= int(input("Your choice :"))
    
    if choice==1:
        course_name=input("Enter course name to add :- ")
        course.append(course_name)

    elif choice==2:
        course_name=input("Enter course name to delete :-")
    
        if (len(course)==0):
            print("nothing in the list, first add something to the list")
            course_name=input("Enter course name to add :- ")
            course.append(course_name)
        else:
            print("Enter course name:")

            if course_name not in course:
                print("course is not in list")

            else:
                course.remove(course_name)
    

    elif choice==3:
        print("exit")
        break

    else:
        print("invalid choice")

    print(course)    