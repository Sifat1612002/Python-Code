import re
x = 'My 2 favourite numbers are 19 and 42'
z = re.findall('[0-9]+', x)
print(z)
y = re.findall('[aeiou] *', x)
print(y)
