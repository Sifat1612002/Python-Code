text = "X-DSPAM-Confidence:    0.8475"
pos = text.find(':')
x = text[pos+4:]
print(float(x))
