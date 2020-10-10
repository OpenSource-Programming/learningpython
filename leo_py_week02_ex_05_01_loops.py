# Exercise 5.1

total = 0
count = 0
average = 0

while True :
    input_from_keyboard = input("Enter a number: ")
    if input_from_keyboard == "done" :
        break

    try:
        current_value = float(input_from_keyboard)
    except:
        print("Invalid input")
        continue

    total = total + current_value
    count = count + 1

if count > 0 :
    average = total / count

print(total, count, average)