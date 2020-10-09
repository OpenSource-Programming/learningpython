count = 0
lines = 0
fname = input('Enter a file name > ')
try:
    fhand = open(fname)
    for line in fhand:
        lines += 1
        if line != '\n':
            linelist = line.split()
            if linelist[0] == 'From':
                count += 1
    print('There were ' + str(count) + ' lines in the file with From as the first word')

except:
    print('File not found.')

# /Users/john/PY4E/Week_3/mbox_short.txt

