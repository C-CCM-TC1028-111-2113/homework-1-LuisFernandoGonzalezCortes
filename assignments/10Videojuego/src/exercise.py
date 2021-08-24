def main():
    #escribe tu código abajo de esta línea
    
   n=int(input("Dame la cantidad de juegos nuevos: "))
   u=int(input("Dame la cantidad de juegos usados: "))

   x=(n*1000)
   y=(u*350)

   f=(x+y)
   print("El total de la compra es: ",f)

if __name__ == '__main__':
    main()
