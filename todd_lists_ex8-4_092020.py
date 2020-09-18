fname = input("Enter file name: ")
fh = open(fname)
lst = list()
global_words = []
for line in fh:
    words = line.split()
    for newword in words:
       if newword in lst:
           continue
       else:
           lst.append(newword)
              
lst.sort()   
print(lst)