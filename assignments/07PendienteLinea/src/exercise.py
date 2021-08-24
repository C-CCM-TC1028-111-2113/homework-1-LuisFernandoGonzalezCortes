def main():
    #escribe tu código abajo de esta línea
    #Lee los datos
    
    x1=float(input("Dar X1: "))
    x2=float(input("Dar X2: "))
    y1=float(input("Dar Y1: "))
    y2=float(input("Dar Y2: "))

    m = ((y2 - y1)/(x2 - x1))
    print("La pendiente es: ",m)


if __name__ == '__main__':
    main()
