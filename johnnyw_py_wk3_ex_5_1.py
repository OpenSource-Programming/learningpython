total = 0.0
count = 0
while True:
    try:
        number = input('> ')
        if number == 'done':
            break
        fn = int(number)
        total += fn
        count += 1
        continue
    except:
        print('Invalid input')
        continue
if count > 0:
    print(str(total) + ' ' + str(count) + ' ' + str(total/count))
else:
    print('0 0 0')
print('Done!')
