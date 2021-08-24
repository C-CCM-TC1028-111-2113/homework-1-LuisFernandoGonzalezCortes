def main():
    #escribe tu código abajo de esta línea
    
    m=float(input("Dame el saldo del mes anterior: "))
    i=float(input("Dame los ingresos: "))
    e=float(input("Dame los egresos: "))
    c=float(input("Dame el número de cheques: "))

    x=(m + i - e - (c * 13))
    f=(x - (x * .075))

    print("El saldo final de la cuenta es: ",f)

if __name__ == '__main__':
    main()
