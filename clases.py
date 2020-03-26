class LamparaDeEscritorio:
    _LAMPS=['''
          .
     .    |    ,
      \   '   /
       ` ,-. '
    --- (   ) ---
         \ /
        _|=|_
       |_____|
    ''',
    '''
         ,-.
        (   )
         \ /
        _|=|_
       |_____|
    ''']
    def __init__(self, is_turned_on):#METODO INSTANCIA propia instancia de la clase , Este es el constructor de la clase
        self._is_turned_on= is_turned_on #varialbes dentro de la clase
        self._display_lamp()

    def turn_on(self):
        self._is_turned_on= True
        self._display_lamp()
      
    def turn_off(self):
        self._is_turned_on= False
        self._display_lamp()
    def _display_lamp(self):
        if self._is_turned_on:
            print(self._LAMPS[0])
        else:
            print(self._LAMPS[1])

def run():
    lamp=LamparaDeEscritorio(is_turned_on=False)
    while True:
        command=str(raw_input('''
        Que deseas hacer

        [p]render
        [a]pagar
        [s]alir'''))
        if command== 'p':
            lamp.turn_on()
        elif command =='a':
            lamp.turn_off()
        else:
            break



if __name__ == "__main__":
    run()
