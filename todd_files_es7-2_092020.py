# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

# Vars for our figuring average
conftotal = 0
confcount = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    numpos = line.find(':')
    numfloat = float(line[numpos+1:].lstrip())
    #print(numfloat)
    confcount +=1
    conftotal += numfloat

confavg = conftotal / confcount
print("Average spam confidence:", confavg)