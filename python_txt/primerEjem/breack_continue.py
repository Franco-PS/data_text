def run():
    # for contacto in range(1000):
    #     if contacto %2 != 0:
    #         continue
    #     print(contacto)

    # for i in range(10000):
    #     print(i)
    #     if i == 5574:
    #         break

    text = input('Escribe un texto: ')
    for letra in text:
        if letra == 'o':
            break
        print(letra)


if __name__ == '__main__':
    run()