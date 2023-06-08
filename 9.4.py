name = input('enter file name:')
handle = open(name)
counts = dict()
lst = list()
for line in handle:
    if line.startswith('From'):
        if line.startswith('From:'):
            continue
        else:
            words = line.split()
            lst.append(words[1])
for word in lst:
    counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)
