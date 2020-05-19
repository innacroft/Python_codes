def enumeracion():
    objetivo = int(input("Introduce un número entero para obtener su raiz: "))
    respuesta = 0

    while respuesta ** 2 < objetivo:
        respuesta += 1

    if respuesta ** 2 == objetivo:
        print(f"La raíz cuadrada de {objetivo} es {respuesta}")
    else:
        print(f"El {objetivo} no tiene una raíz cuadrada exacta")

def aproximacion():
    objetivo = int(input("Introduce un número entero para obtener su raiz: "))
    epsilon = 0.01
    paso = epsilon ** 2
    respuesta = 0.0
    # La primera condicion ...  y la segunda nos ayuda a evitar números negativos
    while abs(respuesta ** 2 - objetivo) >= epsilon and respuesta <= objetivo:
        print(f"respuesta= {respuesta}  |respuesta**2 - objetivo| =  {abs(respuesta ** 2 - objetivo)}")
        respuesta += paso
        respuesta += paso
        # print(f"------------\nNúmero siguiente \nrespuesta= {respuesta} |respuesta**2 - objetivo| =  {abs(respuesta ** 2 - objetivo)}\n------------")

        if abs(respuesta ** 2 - objetivo) >= epsilon:
            print(f"No se encontro raíz cuadrada de {objetivo}")
        else:
            print(f"La raíz cuadrada de {objetivo} es {respuesta}")

def busquedaBinaria():
    objetivo = int(input("Introduce un número entero para obtener su raiz: "))
    epsilon = 0.0001
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2

    while abs(respuesta ** 2 - objetivo) >= epsilon:
        print(f"bajo={bajo}, alto={alto}, respuesta={respuesta}")
        if respuesta ** 2 < objetivo:
            bajo = respuesta
        else:  # if respuesta **2 > objetivo
            alto = respuesta
        respuesta = (alto + bajo) / 2
    print(f"------------------\nbajo={bajo}, alto={alto}, respuesta={respuesta}")
    print(f"La raiz cuadrada de {objetivo} es {respuesta}")

def printMenu():
    print("OPCIONES:\n1. Método por enumeracion")
    print("2. Métdodo por aproximación")
    print("3. Método por busqueda binaria")
    metodo = input("Escoge un método: ")
    return metodo

def selectMenu(metodo):
    if metodo == "1":
        enumeracion()
    elif metodo == "2":
        aproximacion()
    elif metodo == "3":
        busquedaBinaria()
    else:
        print("Número no valido")
        metodo = input("Escoge un número método el 1 y el 3: ")
        selectMenu(metodo)

if __name__ == "__main__":
    metodo = printMenu()
    selectMenu(metodo)