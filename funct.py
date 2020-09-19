def computepay(h, r):
    return h * r


hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
p = computepay(h, r)
if h <= 40:
    print("pay", p)
else:
    p = computepay(h, r) + r / 2 * 5
print("Pay", p)
