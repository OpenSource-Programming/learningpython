# Exercise 5.2

largest = None
smallest = None

while True :
    input_from_keyboard = input("Enter a number: ")		
    if input_from_keyboard == "done" :
         break

    try:
        current_value = int(input_from_keyboard)
    except:
        print("Invalid input")
        continue
		
    if largest is None : 
        largest = current_value
        smallest = current_value
    elif current_value > largest:
        largest = current_value
    elif current_value < smallest:
        smallest = current_value

print("Maximum is", largest)
print("Minimum is", smallest)