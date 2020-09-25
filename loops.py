largest = None
smallest = None
lst = []
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        lst.append(int(num))
    except:
        print('Invalid input')

if lst:
    print('Maximum is', (max(lst)))
    print('Minimum is', (min(lst)))
