print("A*x^2+B*x+C=0:")
A=int(input('Введите А:'))
B=int(input('Введите B:'))
C=int(input('Введите C:'))
D=B**2-4*A*C
if D<0:
    print("Корней нет")
elif D==0:
    x = (-B + D ** 0.5) / (2 * A)
    print(x)
else:
    x1 = (-B + (D**0.5)) / (2 * A)
    x2 = (-B - (D**0.5)) / (2 * A)
    print(x1,x2)