print('Tady je pár čísel:')
for cislo in 8, 45, 9, 21:
    print(cislo)

celkem = 0
for delka_trasy in 8, 45, 9, 21:
    print(f'Jdu {delka_trasy} km do další vesnice.')
    celkem += delka_trasy
print(f'Celkem jsem ušla {celkem} km.')