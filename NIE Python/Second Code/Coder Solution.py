name_age=[]
for i in range(3):
    name=input("Name: ")
    age=int(input("Age: "))
    name_age.append([name,age])
for i in range(len(name_age)):
    print(str(name_age[i][0])+" is "+str(name_age[i][1])+" years old")
