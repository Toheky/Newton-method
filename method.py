from derivate import derivate
from decimal import *

def newton_method(p, x, precision, repeat):
    '''Applied Newton method.'''
    getcontext().prec = 30
    d_p = derivate(p)
    cnt = 0 
    for i in range(repeat):
        cnt += 1
        new_x = Decimal(int(x)) - (Decimal(eval(p))/Decimal(eval(d_p)))
        if abs(new_x-x) < precision:
            return new_x, cnt 
        x = new_x

