name = input('Enter file:')

if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)


authors = dict()

for line in handle:
   if line.startswith("From "):
    author_line = line.split()
    author = author_line[1]

    # Old style 
    #if author in authors:
    #  authors[author] = authors[author] + 1
    #else:
    #  authors[author] = 1

    # Will either add a new element count 1 or increment an existing using idiom  
    authors[author] = authors.get(author,0) +1

#print(authors)

msgcount = None
msgauthor = None

for author,count in authors.items():
  if msgcount is None or count > msgcount:
     msgauthor = author 
     msgcount = count
     #print("author now:", msgauthor)

#print (counts)
print(msgauthor,msgcount)