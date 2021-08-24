
def main():
    edad = int(input("Ingresa tu edad: "))
    if(edad < 18):
        if(edad<=0):
            print("Respuesta incorrecta")
        else:
            print("No cumples requisitos")
    else:       
        #Aquí empieza tu programa...
        id = input("¿Tienes identificación oficial? (s/n): ").lower()
        if(id == "s"):
            print("Trámite de licencia concedido")
        elif(id == "n"):
            print("No cumples requisitos")
        elif(edad <= 0 or (id != "s" or id != "n")):
            print("Respuesta incorrecta")


if __name__ == '__main__':
    main()
