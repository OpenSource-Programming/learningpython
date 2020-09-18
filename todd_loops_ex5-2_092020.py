largest = None
smallest = None
while True:
    num = input("Enter a number: ")		
    if num == "done" : break
	# Check if a valid integer
    try:
        numval = int(num)
    except:
        print("Invalid input")
        continue
		
	# Check if this is the first number entered then set both largest and smallest to first
    if smallest is None: 
        smallest = numval
        largest = numval
    elif numval > largest:
        largest = numval
    elif numval < smallest:
        smallest = numval
    #print(num)

print("Maximum is", largest)
print("Minimum is", smallest)