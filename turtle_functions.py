import turtle 

def main():
    window = turtle.Screen()
    inna= turtle.Turtle()
    make_square(inna)

def make_square(inna):
    #pide el tamaño del cuadrado 
    length=int( raw_input('Square size:'))
    #dibuja la linea 4 veces
    for i in range(4):
        make_line_and_turn(inna,length )
    #cuando turtle termina, espera y no se cierra    
    turtle.mainloop()

def make_line_and_turn(inna,length):
    inna.forward(length)
    inna.left(90)

#define donde empieza el programa 
if __name__=='__main__':
    main() 
