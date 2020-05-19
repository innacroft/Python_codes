
def average_temp(temps):
    sum_temp=0
    for temp in temps:
        sum_temp+=float(temp)
    return sum_temp /len(temps)


if __name__ == "__main__":
    temps=[21,24,24,22,20,23,24]

    average=average_temp(temps)
    print('la temperatura promedio es {}' .format(average))
   #convertir de string a lista:
    casa='casa'
    lista_casa=list(casa)
    print(lista_casa)
    #convertir de lista a string:
    lista_casa=['c','a','s','a']
    str_casa =''.join(lista_casa)
    print(str_casa )```