from random import randrange

cislo = randrange(0, 3)
if cislo == 0:
    print('Kolečko')
elif cislo == 1:
    print('Čtvereček')
else:
    print('Trojúhelník')