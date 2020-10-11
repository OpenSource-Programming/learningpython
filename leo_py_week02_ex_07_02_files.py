# Exercise 7.2

file_name = input("Enter a file name: ")

try :
    file_handler = open(file_name)
except :
    print("File cannot be opened: ", file_name)
    quit()

count = 0
total = 0
average = 0

for line in file_handler :
    if line.startswith("X-DSPAM-Confidence:") :
        extrac_value = line[line.find(":")+1:]
        count = count + 1
        total = total + float(extrac_value)

if count > 0 :
    average = total / count
    print("Average spam confidence:", average)
