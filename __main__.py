#Archivo creado por APC (A Project Creator)
"""
last digit: must not be 0, 8, 9
the sum of the last 7 digits: MUST be divisible by 21 (7)

these rules are provided by the flytech video´s
"""
import random
from sys import argv

for _ in range(int(argv[1])):
    def gen7():
        retornar = ""
        for _ in range(7):
            retornar += str(random.randrange(1000000, 9999999))
        x = retornar[:7]
        return x

    def gen3():
         retornar = ""
         for _ in range(3):
          retornar += str(random.randrange(0,9))
         return retornar



    first3 = gen3() # primeros 3: XXX-xxxxxxx
    last7 = gen7() # ultimos 7: xxx-XXXXXXX
    last7 = int(last7)


    while True: # hasta que last7 no sea divisible por 7 se generan nuevas ""keys""
        if last7 % 10 == 0: # si termina en 0 (key invalida) se repite el proceso
            last7 = gen7() #modulo 10 SIEMPRE el ultimo digito
            last7 = int(last7)
        elif last7 % 10 == 8: # si termina en 8 (key invalida) se repite el proceso
            last7 = gen7()
            last7 = int(last7)
        elif last7 % 10 == 9: # si termina en 9 (key invalida) se repite el proceso
            last7 = gen7()
            last7 = int(last7)
        elif last7 % 7 == 0:
            break
        else:
            last7 = gen7()
            last7 = int(last7)


    print(f"key: {first3}-{last7}")
