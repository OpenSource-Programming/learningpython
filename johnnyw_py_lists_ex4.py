wordlist = []
fhand = open("/Users/john/PY4E/Week_3/romeo.txt")
for line in fhand:
    linelist = line.split()
    for word in linelist:
        if word in wordlist:
            continue 
        else:
            wordlist.append(word)
#wordlist.sort()
print(sorted(wordlist, key=str.lower))
