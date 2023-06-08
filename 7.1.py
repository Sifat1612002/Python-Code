k = input('file name')
try:
    h = open(k)
except:
    print('file connot be opened', k)
    quit()
for l in h:
    l = l.rstrip()
    print(l.upper())
