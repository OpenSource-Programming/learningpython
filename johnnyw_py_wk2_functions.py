# Exercise 6

def computepay(hours, rate):
    return hours * rate

def computegrade(score):

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

    return grade

try:
    hours = float(input('Enter hours worked: '))
except:
    print('Numeric value required.')
    exit()
if hours > 40:
    hours = 40 + (1.5 * (hours - 40))

try:
    rate = float(input('Enter pay rate: '))
except:
    print('Numeric value required.')
    exit()

print('Pay is: ' + str(computepay(hours, rate)))

# Exercise 7

try:
    score = float(input('Enter score: '))
except:
    print('Bad Score')
    exit()

print(computegrade(score))


