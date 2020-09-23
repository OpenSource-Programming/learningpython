# Exercise 1 and 2

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

# Exercise 3

try:
    score = float(input('Enter score: '))
except:
    print('Bad Score')
    exit()

if score < 0.6:
    grade = 'F'
if score >= .6: 
    grade = 'D'
if score >= .7:
    grade = 'C'
if score >= .8: 
    grade = 'B'
if score >= .9:
    grade = 'A'
if score >= 1.0 or score < 0.0:
    grade = 'Bad Score'

print(grade)
