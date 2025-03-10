'''
loop is used to repeat a segment of code....
'''

'''
without loop, print hello 5 times.... 
'''
# print("hello")
# print("hello")
# print("hello")
# print("hello")



'''
with using loop
'''


# for i in range(1, 15, 4):

#     print("hello", i)


'''
range(n) =>  0,1,2,3... n-1 
range(m,n) =>  m, m+1, m+2 ..... n-1 
range(m,n,d) =>   m, m+d, m+2d, m+3d, .... n-1
'''



'''
using loop to sum n integers from termminal input
'''

# ans=0

# for i in range(5):
#     ans = ans + int(input("Enter a number:"))


# print(ans)


'''
using loop to sum n integers from a list
'''

# numbers = [3,4,12,9,56, 0,-3,-5,534,4]

# ans=0

# for i in range( len(numbers) ):
#     ans= ans + numbers[i]    


# print(ans)



'''
for loop, without using range()
'''


'''
directly accessing list
easy to write
no flexibility in choosing index
'''

numbers = [5,2,8,3,1]

for x in numbers:
    print(x)


print('-------------------------------')


'''
accessing list through index using range
felxibility in choosing index
'''
for i in range(0, len(numbers), 2 ):
    print(numbers[i])















