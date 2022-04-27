
# from locale import currency
# from math import trunc


def imprimir_mensaje(type_money):
    print("convierte tu moneda "+ type_money)

def conversor(money,dolar):
    # money_dolar = str(round(int(dolar/money),3))
    money_dolar = str(float(dolar/money))
    print("tienes "+ money_dolar+" dolares")



opcion = int((input(
    """
    Elige la moneda de origen?
    1-Pesos colombianos
    2-Pesos Peruanos
    3-Pesos Mexicanos
    """
)))
money = int(input("Cuanto dinero tienes?"))

if opcion == 1:
    # type_money= "colombiana"
    # dolar = 

    imprimir_mensaje("de colombia a:")
    conversor(money,568)
elif opcion == 2:
    # type_money= "Peruana"

    imprimir_mensaje("Peruanos")
    conversor(28,money)
elif opcion == 3:
    # type_money= "Mexicano"

    imprimir_mensaje("Mexicano")
    conversor(20,money)
else:
    print("No está en la opción")

# def suma(a,b):
#     print('se muma dos numeros')
#     resultado= a + b
#     return resultado

# resultado = suma(5,6)
# print(resultado)