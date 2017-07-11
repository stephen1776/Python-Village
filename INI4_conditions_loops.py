#
'''
Problem

Given: Two positive integers a
and b (a<b<10000

).

Return: The sum of all odd integers from a
through b

, inclusively.
Sample Dataset

100 200

Sample Output

7500

    Hintclick to collapse

    You can use a % 2 == 1 to test if a is odd.

'''
sumOdd = 0
a,b=input().split(' ')

if int(a) > int(b) > 10000:
  print ("Invalid Values!")

elif int(a) == 0 and int(b) == 0:
  print ("0")

else:
  for i in range(int(a),int(b)+1): #this makes it so b actual value w range
    if i %2 != 0:
      sumOdd = sumOdd + i
print (sumOdd)






