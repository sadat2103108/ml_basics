'''
input()
takes a single line from terminal as string
'''

# name = input("Enter your name: ")  

# print("hello", name)

'''
to take other datatype from input, we need to convert it from string
'''


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("answer:", a+b)



#######################################################




'''
arithmatic operator:
'''

a=13
b=8

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)  #float
# print(a//b) #integer
# print(a%b) #modulo , remainder

#to comment , or undo comment everthing, select, then ctrl+/


'''
relational operator
returns, true , or false
>
<
>=
<=
==   true if equal
!=   true of  not equal

'''

# print(13 < 5)  # is 13 less than 5? Ans: false 


'''
logical operator
and: true if both LHS and RHS is true, false otherwise
or: true of any of them is true 
not:  flips the value,      not true  => false,   not false = true

'''


'''
exmaple of or:
find of any number is negative, 
if yes then print found
else print not found
'''

a=5
b=3
c= -1

"instead of doing it like this:"

if(a<0):
    print("found")
elif (b<0):
    print("found")
elif (c<0):
    print("found")
else:
    print("not found")


"you can do it like this: "


if(a<0  or  b<0  or c<0):     #(false or false or true)  => true 
    print("found")
else:
    print("not found")

"you can use and to do the same thing"

if (a>=0 and b>=0 and c>=0):  #true and true and false = false 
    print("not found")
else:
    print("found")

#example of remainder use
#even or odd....

# num = 12
# if (num%2 != 0) :
#     print("its an odd number")
# else:
#     print("its an even number")




a=5
b=3
x =   not (a>b) 

if(x):
    print("ABCD")
else:
    print("XYZ")








