# -*- coding: utf-8 -*-

def calcular_generacion(a_nac):
    if a_nac>=1900:

        if a_nac>=1900 and a_nac<=1914 :
            print('{} --> Interbellum! ' .format(a_nac))
        if a_nac>=1915 and a_nac<=1925 :
            print('{} -->Generacion Grandiosa !'.format(a_nac))
        if a_nac>=1926 and a_nac<=1945 :
            print('{} -->Generacion Silenciosa !'.format(a_nac))
        if a_nac>=1946 and a_nac<=1960 :
            print('{} -->Baby Boomer!'.format(a_nac))
        if a_nac>=1961 and a_nac<=1981 :
            print('{} -->Generacion X !'.format(a_nac)) 
        if a_nac>=1982 and a_nac<=2001 :
            print('{} -->Maldito Millenial !'.format(a_nac))
        if a_nac>=2002 and a_nac<=2020 :
            print('{} -->Awwn, Generacion Z!'.format(a_nac))  
        if a_nac>2020 :
            print('{} -->Pretencioso!, no has ni nacido aun!'.format(a_nac)) 
    else:
        print('Lamentamos informarte que ese año no es valido ')
         

def main():
    print('TEST - A QUE GENERACION PERTENECES ? ')
    a_nac =int(raw_input('Porfavor ingresa tu año de nacimiento -->'))
    calcular_generacion(a_nac)

if __name__ == "__main__":
    main()