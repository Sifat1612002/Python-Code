c = 0
fname = input('enter file name:')
fhand = open(fname)
for line in fhand:
    if line.startswith('From'):
        if line.startswith('From:'):
            continue
        else:
            c = c + 1
            listz = line.split()
            print(listz[1])
print('There were', c, 'lines in the file with From as the first word')
