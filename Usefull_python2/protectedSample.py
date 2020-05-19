def protected(func):
    def wrapper(password):
        if password=='platzi':
            return func()
        else:
            print('Contrasena invalida')
    return wrapper

@protected
def protected_func():
    print('To contrasena es correcta')


if __name__ == "__main__":
    password=str(raw_input('Ingresa tu contrasena:  ')) 
  #  wrapper=protected(protected_func)
   # wrapper(password)

    protected_func(password)