name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

dct = dict()

# Sample Line format we're looking for:
# From gsilver@umich.edu Fri Jan  4 11:11:52 2008
#
for line in handle:
  if line.startswith('From '):
     line_split = line.split()
     tsplit  = line_split[5].split(':')
     hr = tsplit[0]
     dct[hr] = dct.get(hr,0) + 1


# Now we've got a dictionary we can sort it and iterate
for hr,cnt in sorted(dct.items()):
   print(hr,cnt)