def palindrome(word):
    reversed_word = word[::-1]

    if reversed_word == word:
        return True
    return False

if __name__ == '__main__':
    word = input('Escribe una palabra: ')
    word_upper = word.upper()

    result = palindrome(word_upper)
    
    if result is True:
        input('La palabra {} es un palindromo'.format(word))
    else:
        input('La palabra {} no es palindormo'.format(word))