# Exercise 7.1

file_name = input("Enter a file name: ")

try :
    file_handler = open(file_name)
except :
    print("File cannot be opened: ", file_name)
    quit()

for line in file_handler :
    print(line.upper().rstrip())
