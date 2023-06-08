name = input('enter:')
fhand = open(name)
dic1 = dict()
lst = list()

for line in fhand:
    if line.startswith('From'):
        if line.startswith('From:'):
            continue
        else:
            words = line.split()
            str1 = ''.join(words[5])
            lst.append(str1[0:2])
for word in lst:
    dic1[word] = dic1.get(word, 0) + 1
for i, y in sorted(dic1.items()):
    print(i, y)
