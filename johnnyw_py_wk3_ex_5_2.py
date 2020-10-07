max = 0
min = 0
first = True
while True:
    try:
        number = input('> ')
        if number == 'done':
            break
        fn = int(number)
        if fn > max:
            max = fn
        if first == True or fn < min:
            min = fn
        first = False
        continue
    except:
        print('Invalid input')
        continue
print(str(max) + ' ' + str(min))
print('Done!')
