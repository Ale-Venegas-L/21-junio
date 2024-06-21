price = 15800
def min_Max(n, min, max):
    while True:
        if n < min or n > max:
            print("Número invalido.")
        else:
            return
        
def discount(n):
    if n >= 18 and n <= 65:
        print("Tiene un descuento!")
        if n >= 18:
            newPrice = price - (price*0.20)
        else:
            newPrice = price - (price*15)
    else:
        pass
