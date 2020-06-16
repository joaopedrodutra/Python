import math
a = float(input("Informe o valor de A: "))
b = float(input("Informe o valor de B: "))
c = float(input("Informe o valor de C: "))

delta = b * b - 4 * a * c

if a == 0 or delta < 0:
    print("Na equação {}x² + {:.0f}x + {:.0f} = 0, não existem valores reais para x".format(a, b, c))
elif delta == 0:
    x = (-b + math.sqrt(delta)) / (2 * a)
    print("Na equação {:.0f}x² + {:.0f}x + {:.0f} = 0, x = {:.2f}".format(a, b, c,x))
elif delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print("Na equação {:.0f}x² + {:.0f}x + {:.0f} = 0, x1 = {:.2f} e x2 = {:.2f}".format(a, b, c, x1, x2))


