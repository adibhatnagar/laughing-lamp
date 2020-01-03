# The symbol '#' is used to comment statements but only outside of functions such as print(), input(), etc
# If inside a function '#' will be considered as an input or variable depending on the function
# There are no multi-line comments in Python

name=input("Enter your name: ")  #Only accepts strings as input

#Writing only input() will only allow for strings or characters to be accepted

age=int(input("Enter your age: ") ) #Only accepts integers as input

#Parsing input() as int() tells the computer that the input will only be an integer

height=float(input("Enter your height in meters: "))  #Only accepts float i.e decimals as input

#Float also accepts integers  but when outputing float  it will output as a decimal
#You can specify the number of decimal points to print the float till using print(round(Number, Number_of_decimal_points))

print("Hi "+str(name)+". Wow you're "+str(height)+"  meters tall! That's awesome for "+str(age)+"  years old!")

#You can use either double-inverted commas " "  or single-inverted commas  '  ' inside the print() function
#You need to parse variable as a string to print them
