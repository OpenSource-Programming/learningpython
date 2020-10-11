# Exercise 8.4

file_name = input("Enter a file name: ")

try :
    file_handler = open(file_name)
except :
    print("File cannot be opened: ", file_name)
    quit()

list_of_words = list()

for line in file_handler :
    words = line.split()
    for word in words :
        if word not in list_of_words :
            list_of_words.append(word)

list_of_words.sort()
print(list_of_words)
