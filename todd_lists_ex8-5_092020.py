fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

count = 0

fh = open(fname)
for line in fh:
  #print(line.rstrip())
  if line.startswith('From '):
    #print(line) 
    elements = line.split() 
    print(elements[1]) 
    count += 1

print("There were", count, "lines in the file with From as the first word")