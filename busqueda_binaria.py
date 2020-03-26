def binary_search(numbers,number_to_find,low,high):
    if low > high: #ya se recorrio la lista y el numero no aparece
        return False

    mid=(low + high) / 2 #se realiza la division de los indices
    
    if numbers[mid]==number_to_find: #si el numero de indice mid es igual al numero que buscamos
        return True
    elif numbers[mid]>number_to_find: #si el numero de la mitad es mayor al numero buscado
        return binary_search(numbers,number_to_find,low,mid - 1) #inicie recursividad con la primera mitad, desde  inicio hacia el centro
    else:
        return binary_search(numbers,number_to_find,mid + 1,high) #si el numero de la mitad es menor al numero buscado, inicie recursividad del centro hacia el final

if __name__ == "__main__":
    numbers = [1,3,4,5,6,9,10,11,25,27,28,34,36,49,51] #lista de numeros ordenados inicial
    number_to_find = int(raw_input('Ingresa un numero: ')) #solicita  al usuario un numero para buscarlo en la lista anterior
    result= binary_search(numbers,number_to_find,0, len(numbers)-1) 
    if result is True:
        print('El numero esta en la lista')
    else:
        print('El numero no esta en la lista')