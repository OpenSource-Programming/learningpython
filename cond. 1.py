hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
if h <= 40:
    pay = h * r
    print(pay)
else:
    pay = h * r
    extra_pay = (pay) + r / 2 * 5
    print(extra_pay)
