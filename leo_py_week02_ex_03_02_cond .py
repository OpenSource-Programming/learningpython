# Exercise 3.2

hours = input("Enter Hours: ")
rate = input("Enter Rate: ")

try:
    hours = float(hours)
    rate = float(rate)
except:
    print("Error, please enter numeric input")
    quit()

if hours > 40 :
    pay_regular = hours * rate
    pay_overtime = (hours - 40.0) * (rate * 0.5)
    pay_total = pay_regular + pay_overtime
else:
    pay_total = hours * rate

print("Pay:", pay_total)
