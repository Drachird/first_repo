from random import randrange

soucet = 0
while soucet < 21:
    print(f'Máš {soucet}.')
    otazka = input('Chceš pokračovat? ')
    if otazka == 'ano':
        karta = randrange(2, 11)
        print(f'Otočil jsi {karta}')
        soucet += karta
    elif otazka == 'ne':
        break
    else:
        print('Nerozumím!')

if soucet == 21:
    print('Gratuluji! Vyhrál jsi!')
elif soucet > 21:
    print(f'Smůla! {soucet} bodů je moc!')
else:
    print(f'Chybělo jen {21 - soucet} bodů!')