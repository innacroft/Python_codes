for i in range(30):
  if i % 3 != 0: #si  i no es exactamente divisible en 3
    continue  #sigue dentro de la iteracion
  else: # si i es divisible 
    print(i**2)  #i es elevado al cuadrado 

for i in range(30):
  if i % 3 == 0: # si i es exactamente divisible en 3
    print(i**2)  #i es elevado al cuadrado 
  elif i==22: # si i es igual a 22
    break   #termina la iteracion