from dolgozok import *
global uj_dolgozo


def main():
    
    load_from_file('fizetesek.csv')
    print(f'2. feladat: Dolgozók száma: {len(dolgozok_listaja)}')
    uj_dolgozo = str(input('3. feladat: Dolgozó neve: '))
    uj_dolgozo_hozzaadasa('fizetesek.csv', uj_dolgozo)
    uj_fizetes = int(input('4. feladat: A dolgozó fizetése:'))
    # try:
        # fizetes_hozzaadas('fizetesek.csv', uj_fizetes)
    # except not fizetes_hozzaadas('fizetesek.csv', uj_fizetes):
    #    print('Ilyen nevű dolgozó nincs a cégnél.')
    legtobb = keres()
    print(f'5. feladat: Legtöbbet kereső dolgozó:{legtobb.nev}, fizetése: {legtobb.fizetes} Ft')
    print('6. feladat:')
    for k in dolgozok_listaja:
        if k.fizetes > 632364:
            print(k.nev)
    
    mentes('fizetesek_uj.csv')
main()