from kuldetes import *

kuldetesek : list[kuldetes] = []
def main():
    beolvas('kuldetesek.csv')
    print(f'3. feladat:  összesen {len(kuldetesek)} alkalommal indítottak űrhajót')
    print(f'4. feladat: {utasok_szama()} utas indult az űrbe összesen.')
    print(f'5. feladat: Összesen {szamlal(5)} alkalommal küldtek kevesebb mint 5 embert az űrbe')
    print(f'6. feladat: {utolso()} asztronauta volt a Columbia fedélzetén annak utolsó útján ')
    leghossz = leghosszabb()
    print(f'7. feladat: A leghosszabb ideig a {leghossz.nev} volt az űrben a(z) {leghossz.kod} küldetés során. \n Összesen {leghossz.ossz} órát volt távol a Földtől')
    print(f'8. feladat: ')
    evszam = int(input('Évszám: '))
    print(f'Ebben az évben {kuldetes_szama(evszam)} volt')
    print(f'9. feladat: A küldetések {kennedy()}%-a fejeződött be a Kennedy űrközpontban.')

def kennedy():
    kennedy = 0
    for k in kuldetesek:
        if k.legitamaszpont == 'Kennedy':
            kennedy += 1
    return kennedy / len(kuldetesek) * 100


def kuldetes_szama(evszam):
    osszes = 0
    for k in kuldetesek:
        if k.ev == evszam:
            osszes += 1
    return osszes



def leghosszabb():
    leghossz = kuldetesek[0]
    for k in kuldetesek:
        if k.ossz > leghossz.ossz:
            leghossz = k
    return leghossz
            

    
    

def utolso():
    for k in kuldetesek:
        if k.datum == '2003.01.16':
            return k.letszam
    



def szamlal(maximum):
    hany = 0
    for k in kuldetesek:
        if k.letszam < maximum:
            hany += 1
    return hany



def utasok_szama():
    utasok = 0
    for kutyafule in kuldetesek:
        utasok += kutyafule.letszam
    return utasok


def beolvas(filename):
    file = open(filename, 'r', encoding='utf-8')
    for sor in file:
        kuldetesek.append(kuldetes(sor.strip()))
    file.close()

main()