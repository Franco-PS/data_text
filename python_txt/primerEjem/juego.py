import random


def run():
    num_aleatoreo = random.randint(1,100)
    num_elegido = int(input('Elige un número del 1 al 100: '))
    while num_aleatoreo != num_elegido:
        if num_elegido < num_aleatoreo:
            print('Busca un número más grande')
            # num_elegido= int(input('Elige otro número:   ')) 
        else:
            print('Busca un número menor')

        num_elegido= int(input('Elige otro número: '))
    print('excelente el número pensado es el correcto')

if __name__ == '__main__':
    run()
