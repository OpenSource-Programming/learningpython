#VES Exercise 2
inp = input('Enter your name: ')
print('Hello' , inp)
print()

#VES Exercise 3
hours = input('Enter Hours: ')
rate = input('Enter Rate: ')
pay = int(hours) * float(rate)
print('Pay:' , pay)
print()

#VES Exercise 4
width = 17
height = 12.0
print('Assume width is 17 and height is 12.0')
width1=width//2
print('Width//2:', width1)
print(type(width1))
print()
width2=width/2.0
print('Width/2.0:', width2)
print(type(width2))
print()
height1=height/3
print('Height/3:', height1)
print(type(height1))
print()
var=1+2*5
print('1+2*5=', var)
print(type(var))
print()

#VES Exercise 5
cels = input('Enter degrees Celsius: ')
fahr = float(cels) * 9/5 +32
print('That is', fahr , 'degrees Fahrenheit')