import numpy as np
def func(method) :
    print(method(2))

def met(x) :
    return x*x

func(met)
print(type(met))