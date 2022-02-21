print('Odpovídej "ano" nebo "ne".')

# Lepší je deklarovat proměnné na začátku, pro přehlednost
stastna_retezec = input('Jsi šťastná? ')
bohata_retezec = input('Jsi bohatá? ')

# Jednodušší if-else systém, zajímá tě pouze ANO, aby ti to vrátilo True, řetězec převedeš na malá písmenka abys nemusel
# řešit případy jako Ano, ANo, aNO, aNo atp., tyto případy ti vždy vrátí True.
STASTNA: bool = stastna_retezec.lower() == "ano"
BOHATA: bool = bohata_retezec.lower() == "ano"


if BOHATA and STASTNA:
    print('Gratuluji!')
elif BOHATA:
    print('Zkus se víc usmívat!')
elif STASTNA:
    print('Zkus míň utrácet.')
else:
    # Tady ti je celkem jedno jestli ti vše ostatní vrátí False, pořád ti to vypíše To je mi líto, moc tady nepotřebuješ
    # error handling
    print('To je mi líto.')
