
#     Variables and Some Arithmeticclick to expand
# example 
#a = 324
#b = 24
#c = a - b
#print('a - b is', c)
'''
Ex:
Given: Two positive integers a and b (a<b<10000).
Return: The sum of all odd integers from a through b, inclusively.
Sample Dataset:
100 200
Sample Output:
7500

'''

#Problem

#Given: Two positive integers a
#and b
#, each less than 1000.
#Return: The integer corresponding to the square of the hypotenuse of the right triangle whose legs have lengths a
#and b.


a = 978
b = 938
c = 0


if int(a)>10000 or int(b)>10000:
  print("Invalid Values Encountered!") 

elif int(a)==0 and int(b)==0:
  print("0")

else: 
    print('c =', a*a + b*b)






