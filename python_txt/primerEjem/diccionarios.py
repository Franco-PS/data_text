def run():
    mi_diccionario = {
        # llaves valores
        'llave1':1,
        'llave2':2,
        'llave3':3,
    }
    print(mi_diccionario)
    print(mi_diccionario['llave2'])

    for pais in mi_diccionario.keys():
        print(pais)

    for pais in mi_diccionario.values():
        print(pais)
    for pais,poblacion in mi_diccionario.items():
        print(pais + ' tiene '+ str(poblacion)+ ' habilitantes')


        
if __name__ == '__main__':
    run()