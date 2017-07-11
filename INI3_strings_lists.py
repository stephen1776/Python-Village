
# 
'''Problem

Given: A string s
of length at most 200 letters and four integers a, b, c and d.

Return: The slice of this string from indices a
through b and c through d (with space in between), inclusively. In other words, we should include elements s[b] and s[d]
in our slice.
Sample Dataset

HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain.
22 27 97 102

Sample Output

Humpty Dumpty
'''

a = 6
b = 11
c = 46
d = 58
x2 = 'RdUi8ZMarecaaJOFe1uY40LXVKN2eywlnaEXJFGlD1qlfrmultifasciata7Jsx7shczimp2jBkDKBBdksMqbIrDLpu1soOIwZeReRfnAaMsjHZCiQEe7Ot7s65FRWFF1hV4hMAtlmW4SCrwIVFSsyG0yVSVWJlDladRP'
stringc = (x2)
print(stringc[int(a):int(b) + 1], stringc[int(c):int(d) + 1])




