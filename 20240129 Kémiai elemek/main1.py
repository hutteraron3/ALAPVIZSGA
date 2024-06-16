from Elements import *


def menu() -> None:
    load_from_file('felfedezesek.csv')
    print(f'Elemek száma: {len(elements)}')
    print(f'Ókorban felfedezett elemek száma: ')


menu()