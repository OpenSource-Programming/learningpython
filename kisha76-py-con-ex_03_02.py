xh = input("Enter Hours: ")
xr = input("Enter Rate: ")
fh = float(xh)
fr = float(xr)
print(fh, fr)
if fh >40:
    print("Overtime")
    #reg = fr * fh
    reg = fh * fr
    otp = (fh - 40.0) * (fr * 1.5)
    print(reg, otp)
    xp = reg + otp
else:
    print("Regular")
    xp = fh * fr
print("Pay:",xp)
