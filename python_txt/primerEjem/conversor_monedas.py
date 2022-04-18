tipo_moneda= """
Elige el tipo de moneda que tienes
1 Moneda Colombiana
2 Moneda Peruana
3 Moneda Mexicana
"""
option = int(input(tipo_moneda))

if option == 1:
    pesos = float(input("¿Cuántos pesos colombianos tienes? "))
    valor_dolar = pesos/3878
    dolares = round(valor_dolar,2)
    dolares = str(dolares)
    print("tienes $"+ dolares+ " dolares")
elif option == 2:
    pesos = float(input("¿Cuántos pesos Peruanos tienes? "))
    valor_dolar = pesos/3878
    dolares = round(valor_dolar,2)
    dolares = str(dolares)
    print("tienes $"+ dolares+ " dolares")
elif option == 3:
    pesos = float(input("¿Cuántos pesos Mexicanos tienes? "))
    valor_dolar = pesos/3878
    dolares = round(valor_dolar,2)
    dolares = str(dolares)
    print("tienes $"+ dolares+ " dolares")
else:
    print("Ingres una opción real")
