from küldetés import *

kuldetesek_listaja: list[Kuldetes] = []

def main():
    beolvas('kuldetesek.csv')
    print(f'3. feladat: összesen {len(kuldetesek_listaja)} alkalommal indítottak űrhajót')
    print(f'{utasok_szama()} utas indult az űrbe összesen.')
    print(f'{szamlal(5)} alkalommal indult utas az űrbe.')
    print(f'{utolso("2003.01.16")} db asztronauta volt a Columbia utolsó útján.')
    leghosszabb = leghosszabb_ido()
    print(f'{leghosszabb.nev} volt sokáig az űrben {leghosszabb.kod} küldetés gyanánt.\n Összesen {leghosszabb.osszes} órát volt az űrben.')
    evszam = int(input('Évszám: '))
    print(f'{kuldetes_szama(evszam)} db küldetés volt.')
    print('8. feladat')
    statisztika_fajlba('misszió.csv')
def utasok_szama():
    utasok = 0
    for k in kuldetesek_listaja:
        utasok += k.letszam
    return utasok

def beolvas(filename):
    file = open(filename, 'r', encoding='utf-8')
    for row in file:
        kuldetesek_listaja.append(Kuldetes(row))
    file.close()

def szamlal(max):
    darab = 0
    for k in kuldetesek_listaja:
        if k.letszam < max:
            darab += 1
    return darab

def utolso(utolso):
    for k in kuldetesek_listaja:
        if k.datum == utolso:
            return k.letszam

def leghosszabb_ido():
    leghosszabb = kuldetesek_listaja[0]
    for k in kuldetesek_listaja:
        if leghosszabb.osszes < k.osszes:
            leghosszabb = k
            return leghosszabb
    return leghosszabb

def kuldetes_szama(evszam):
    osszes = 0
    for k in kuldetesek_listaja:
        if k.ev == evszam:
            osszes += 1
    return osszes

def kennedy():
    osszes = 0
    for k in kuldetesek_listaja:
        if k.legitamasz == 'Kennedy':
            osszes += 1
        return kennedy / len(kuldetesek_listaja) * 100
    
def statisztika_fajlba(filename):
    stat = {}
    for k in kuldetesek_listaja:
        if k.nev not in stat.keys():
            stat[k.nev] = k.osszes
        else:
            stat[k.nev] += k.osszes
    
    file = open(filename, 'w', encoding='utf-8')

    for key, value in stat.items():
        file.write(f'{key}\t{round(value / 24)}\n')

    file.close()
main()