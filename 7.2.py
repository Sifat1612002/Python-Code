c = 0
b = 0
b = float(b)
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        a = float(line[20:26])
        b = b + a
        c = c + 1


print("Average spam confidence:", b/c)
