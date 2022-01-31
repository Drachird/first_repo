def obsah_obdelnik(a, b):
    if a > 0 and b > 0:
        obsah = a * b
        print(f'Obsah obdélníka se stranami {a} cm a {b} cm je {obsah} cm2.')
    else:
        print('Zadat tam kladné číslo nebyl dobrý nápad.')

obsah_obdelnik(9, 5)
obsah_obdelnik(-1, 10)

def obsah_obdelnik_zpet(a, b):
    obsah = a * b
    return obsah

dum = obsah_obdelnik_zpet(100, 500)
print(f'Tvůj dům má {dum} cm2 obdélníků.')

