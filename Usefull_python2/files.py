
import os

def read_(file_):
    with open(file_ , 'r') as f:
        for line in f:
            print(line)
    f.close()

def write_(file_,data_):
    with open(file_,'w') as f:
        f.write(str(data_))
        f.close()

def edit_(file_ , old_word, new_word):
    with open(file_,'r') as f:
        count=0
        filedata=f.read()
        filedata = filedata.replace(old_word, new_word,count)
        if count != 0:
            with open(file_, 'w') as f:
                f.write(filedata)
                f.close()
        else:
            print ('La palabra {}, no existe en este archivo' .format(old_word))


def append_(file_, data_):
    with open(file_,'a') as f: 
        f.write(data_)
        f.close()       
     

if __name__ == "__main__":
    File_=raw_input('Ingresa el nombre del archivo:')
    currentDirectory = os.getcwd() #obtiene la ruta del archivo sobre el cual me encuentro
    file_=currentDirectory+"\\"+File_
    print(file_)
    try:
        f = open(file_)
    except IOError:
        print('El archivo no existe')
        print ('Deseas crearlo?:')
        print ('[s]i')
        print ('[n]o')
        resp=raw_input('')
        if resp== 's':
            
            file = open(file_, "w") 
            file.write('') 
            file.close() 
        else:
            print('Lo siento, pero el archivo no existe.. no puedo hacer nada.. adios.')
            exit(0)

    print ('Que deseas hacer con el archivo:')
    print ('[1]Leer')
    print ('[2]Escribir')
    print ('[3]Editar (buscar una palabra y la reemplazarla )')
    print ('[4]Agregar linea a texto existente')
   
    file_action=raw_input('')
    if file_action:
        if int(file_action)>0 and  int(file_action)<5:

            if int(file_action) == 1:
                read_(file_)
            if int(file_action) == 2:
                data_=raw_input('Ingrese el texto a escribir: ')
                write_(file_,data_)
            if int(file_action) == 3:
                old_word=raw_input('Ingrese palabra a buscar ')
                new_word=raw_input('Ingrese palabra nueva ')
                edit_(file_,old_word, new_word)
            if int(file_action) == 4:
                data_=raw_input('Texto o palabra a agregar: ')
                append_(file_, data_)
        else:
            print ('Esa opcion no es correcta')
    else:
        print ('Esa opcion no es correcta')
