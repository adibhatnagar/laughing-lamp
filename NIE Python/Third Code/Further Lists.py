list_1=['Apple','Dell','HP','LG','Samsung','Acer','MSI','Asus','Razer'] #declares list containing names of laptop makers as strings
list_2=[1,2,3,3,3,4,5,5,6,7,8,8,8,8,9] #declares list containing integers

#Remember list elements have index starting from 0 so for list_1 the element 'Apple' has index 0
#If you store an element of a list using inverted commas then it is stored as a string
#For example, list_temporary=['1','2','3'] contains the first three integers as strings

#for the following code uncomment each line to see what it does
#after observing comment that line re-run code after saving this code

#print(list_2.count(8))
#print(list_2.count(3))
#print(list_1.count('Apple'))
#print(list_2.index(3))
#print(list_2.index(5))
#print(list_2.index(8))
#print(list_2.pop(0))
#print(list_2.pop(5))
#print(list_2.remove(3)) 
#print(list_1.reverse())
#print(list_1.sort())


#follow the next 4 lines by uncommenting and recommenting two lines at once
#list_1.insert(0,'Lenovo')
#print(list_1)
#print(list_1.remove('Lenovo'))
#print(list_1)


#this code prints the list_1 by accessing index through list_2
# to compare values of strings, integers, etc we use comparators
#for example '!=' is comparator for 'not-equal-to'
# '==' is comporator for 'equal'
# '>' and '<' are 'less/greater than' comparators


#follow the next six lines one after other or else you will get an error message
#for i in range(0, (len(list_2)-1)):
#   if list_2[i]<list_2[i+1]:
#        print(list_2[i], list_1[list_2[i]-1])
#    if i+1==len(list_2)-1:
#        if list_2[i] != list_2[i+1]:
#            print(list_2[i+1], list_1[list_2[i]])


