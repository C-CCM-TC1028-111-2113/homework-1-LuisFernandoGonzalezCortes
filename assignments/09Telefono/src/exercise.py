def main():
    #escribe tu código abajo de esta línea
    #Leer los datos
    m=int(input("Dame el número de mensajes: "))
    g=float(input("Dame el número de megas: "))
    i=int(input("Dame el número de minutos: "))

    c=((m + g + i) * (.8))
    print("El costo mensual es: ",c)

if __name__ == '__main__':
    main()
