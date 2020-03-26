import random 

IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']

words = ['santiago', 'yesid','dayana'
		'hematoma','desden','pericia','toxicidad','delito'
		'pugnaz','desfachatez','reliquia','perentorio','consuetudinario']

def drawBoard(hidden_word,attempt):
	print ('A H O R C A D O ')
	print ('----------------')
	print ('')
	print (IMAGES[attempt])
	print ('')
	
def rep(word, hidden_word, current_letter):
 
	for i, letter in enumerate(word):
		if letter == current_letter:
			hidden_word[i] = current_letter

	return hidden_word


def random_word():
	idx = random.randint(0,len(words)-1)

	return words[idx]

def tryagain():

	option = str(raw_input('Jugar de nuevo s or  n  '))
	if option == 's':
		return True 
	elif option == 'n': 
		return False
	else:
		print('Ingresa un caracter valido')
		tryagain ()


def word_guess():

	print('BIENVENIDO AL AHORCADO')

	retry = False 
	word = random_word()
	hidden_word = ['-']*len(word)
	used_letters = []
	attempt = 0 
	while True: 
		drawBoard(hidden_word, attempt)
		print ('*--*'*len(word))
		print (hidden_word)
		print ('')
		current_letter = str(input('Ingresa una letra: '))

		if current_letter in word and not current_letter in used_letters: 
			hidden_word = rep(word, hidden_word, current_letter)
			used_letters.append(current_letter)
			word.replace(current_letter, '-')

			if not'-'in hidden_word and attempt < len(IMAGES) -1:
				print ('F E L I C I T A C I O N E S!!!')
				print ('')
				print ('La palabra es {}'.format(''.join(hidden_word)))
				print ('')
				retry = tryagain()
				if retry:
					word_guess()
					break
				elif not retry:
					print ('H A S T A L U E G O!!!')
					break 

		elif current_letter in used_letters:
			print ('La letra ya esta en uso, prueba otra')

		else:
			attempt = attempt+1 
			used_letters.append(current_letter)
			if attempt == len(IMAGES)-1:
				print ('G A M E O V E R')
				print ('')
				retry = tryagain()
				if retry:
					word_guess()
					break
				elif not retry:
					print ('H A S T A L U E G O!')
					break 

if __name__=='__main__':
	word_guess()