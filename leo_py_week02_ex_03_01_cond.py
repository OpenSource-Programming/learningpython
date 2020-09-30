# Exercise 3.1

hours = input("Enter Hours: ")
rate = input("Enter Rate: ")

hours = float(hours)
rate = float(rate)

if hours > 40 :
    pay_regular = 40 * rate
    pay_overtime = (hours - 40.0) * (rate * 1.5)
    pay_total = pay_regular + pay_overtime
else:
    pay_total = hours * rate

print("Pay:", pay_total)
