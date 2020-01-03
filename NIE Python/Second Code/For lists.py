volunteer_arr=[] #declares new list called 'volunteer_arr'

#A list is simply an array that stores all types of data

for i in range(0,10): #this is the implementation of the FOR loop in Python
    #the range() specifies the number inside the brackets as the number of iterations for which the loop will run
    #range(0,10) means that the iterations start from 0 and end at 9 thus repeating 10 times. This can also be written as range(10)
    name=input("Enter name:")
    volunteer_arr.append(name)
    #As you will notice the variable used in the loop i.e 'i' has not been used
    #This is because it can be thought of as a counter which acts to break the loop once the end value is reached
for j in range(10):
    print("List of Volunteers:-")
    print(str(j+1)+". "+str(volunteer_arr[j])) #j starts from 0 so when listing from 1 to 10 you use j+1
    
