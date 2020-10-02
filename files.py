fname = input("Enter file name: ")
fh = open(fname)
count = 0
big = 0
big = float(big)
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        a = float(line[20:26])
        big = big + a
        count = count + 1
print("Average spam confidence:", big/count)
