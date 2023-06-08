name = 'mbox-short.txt'
handle = open(name)
di = dict()
li = list()
for line in handle:
    if line.startswith('From'):
        if line.startswith('From:'):
            continue
        else:
            words = line.split()
            li.append(words[1])
print(li)
for word in li:
    di[word] = di.get(word, 0)+1
print(di)
bw = None
bc = None
for word, count in di.items():
    if bc is None or count > bc:
        bw = word
        bc = count
print(bw, bc)
