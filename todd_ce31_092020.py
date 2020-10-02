hrs = input("Enter Hours:")
rate = input("Enter rate:")
h = float(hrs)
rate = float(rate)
if h <= 40:
     pay = h * rate
else:
    overtime = h - 40
    pay = 40 * rate + overtime * (rate * 1.5)
    
print(pay)
