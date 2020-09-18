def computepay(h,r):    
    if h <= 40:
     pay = h * r
    else:
     overtime = h - 40
     pay = (40 * r) + (overtime * (r * 1.5))
        
    return pay


hrs = input("Enter Hours:")
rate = input("Rate:")
hrs = float(hrs)
rate = float(rate)

p = computepay(hrs,rate)
print("Pay",p)