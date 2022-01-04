#!/usr/bin/python3


def weight_average(my_list=[]):
    if my_list is None:
        return 0
    else:
        numerador = 0
        denominador = 0
        for tuple in my_list:
            (score, weight) = tuple
            numerador += (score * weight)
            denominador += weight
        return (numerador/denominador) if denominador > 0 else 0
