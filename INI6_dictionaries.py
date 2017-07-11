
#
'''
Intro to Python dictionary
Problem

Given: A string s

of length at most 10000 letters.

Return: The number of occurrences of each word in s

, where words are separated by spaces. Words are case-sensitive, and the lines in the output can be in any order.
Sample Dataset

We tried list and we tried dicts also we tried Zen

Sample Output

and 1
We 1
tried 3
dicts 1
list 1
we 2
also 1
Zen 1

    Hintsclick to collapse

    To iterate over the words in a string, you can split it at each occurrence of empty space as follows:

    for word in str.split(' '):
        print word

    For a pretty representation when outputting a dictionary, you can use the built in .items() function:

    for key, value in dict.items():
        print key
        print value


'''




string = []
frequency = []
d = {} # create an empty dictionary with d = {}
string = input(' ').split(' ')

for words in string:
    frequency.append(string.count(words))
  
for i in range(0,len(string)):
    d[string[i]] = frequency[i]

for k, v in d.items():
    print(k, v)



