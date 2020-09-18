text = "X-DSPAM-Confidence:    0.8475";
numpos = text.find(':')
numval = float(text[numpos+1:].lstrip())
print(numval)