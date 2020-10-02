# Exercise 2.3

try:
    hours = float(input('Enter hours worked: '))
except:
    print('Numeric value required.')
    exit()
if hours > 40:
    ot_hours = hours - 40
    hours = 40
else:
    ot_hours = 0.0
try:
    payrate = float(input('Enter pay rate: '))
except:
    print('Numeric value required.')
    exit()
pay = hours * payrate + (1.5 * ot_hours * payrate)
print('Pay is: ' + str(pay))

