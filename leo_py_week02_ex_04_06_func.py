# Exercise 4.6

def computepay(h, r) :
    if h > 40 :
        pay_regular = 40 * r
        pay_overtime = (h - 40.0) * (r * 1.5)
        pay_total = pay_regular + pay_overtime
    else:
        pay_total = h * r
    return pay_total

hours = input("Enter Hours: ")
rate = input("Enter Rate: ")

try:
    hours = float(hours)
    rate = float(rate)
except:
    print("Error, please enter numeric input")
    quit()

p = computepay(hours, rate)
print("Pay", p)
