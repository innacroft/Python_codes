# -*- coding: utf-8 -*-
def currency_converter(amount):
    mex_to_col_rate=175.56
    return mex_to_col_rate * amount

def run():
    print('C U R R E N C Y    C O N V E R T E R')
    print('Mexican to Colombian pesos converter\n')
    amount=float(raw_input('Please enter the amount of Mexican pesos to convert -->'))
    currency_converter(amount)
    result = currency_converter(amount)
    print('${} mexican pesos = ${} colombian pesos\n'.format(amount,result))


if __name__ == "__main__":
    run()

    