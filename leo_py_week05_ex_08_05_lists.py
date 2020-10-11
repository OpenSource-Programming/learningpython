# Exercise 8.5

file_name = input("Enter a file name: ")

try :
    file_handler = open(file_name)
except :
    print("File cannot be opened: ", file_name)
    quit()

count = 0

for line in file_handler :
    if line.startswith("From") and not line.startswith("From:") :
        words = line.split()
        print(words[1])
        count = count + 1

if count > 0 :
   print("There were", count, "lines in the file with From as the first word")
