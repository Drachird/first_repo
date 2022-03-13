# Vždycky je lepší takto deklarovat konstantu na začátku, protože když to uděláš takto, tak ti stačí změnit jednu
# proměnnou a ta se později změní všude, abys potom nemusel upravovat každý řádek, který to číslo má.
KONSTANTNI_CISLO = 3

cislo = int(input(f'Zadej číslo, přičtu k němu {KONSTANTNI_CISLO}: '))
if cislo == 0:
    print('Jé, to je jednoduché!')
print(cislo, f'+ {KONSTANTNI_CISLO} =', cislo + KONSTANTNI_CISLO)

cislo += 1
print(cislo)
