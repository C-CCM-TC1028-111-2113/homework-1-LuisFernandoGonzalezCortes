def main():
    #escribe tu código abajo de esta línea
    
    p=int(input("Dame el número de palabras: "))

    if p<475:
        x=54
    else:
        x=(60*(int(p/475)))
        print("El costo de la publicación es: ",x)


if __name__ == '__main__':
    main()
