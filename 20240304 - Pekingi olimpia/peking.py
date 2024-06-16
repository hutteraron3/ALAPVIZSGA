from olimpia import Olimpia

versenyzok : list[Olimpia] = []

def main():
    read('torna.csv')
    print(f'3. feladat: Összesen {len(versenyzok)} versenyző indult a versenyen')
    print(f'4. feladat: Korláton {aranyerem().nev} szerezte az aranyérmet.')
    rajtszam = input('5. feladat: Kérem a versenyző rajtszámát: ')
    if kereses(rajtszam):
        print(f'A {rajtszam} rajtszámú versenyző elért eredménye: {kereses(rajtszam).gyuru}')
    else:
        print('Nincs ilyen rajtszám.')
    print('6. feladat: lóversenyben nem értek el helyezést: ')
    lolenges()
    stat = statisztika()
    for key,value in stat.items():
        print(f'\t{key}: {value} fő')
def read(filename: str):
    file = open(filename, 'r', encoding='utf-8')
    file.readline()
    for row in file:
        versenyzok.append(Olimpia(row))
    file.close()

def aranyerem():
    arany = versenyzok[0]
    for v in versenyzok:
        if arany.korlat < v.korlat:
            arany = v
    return arany

def kereses(rajtszam):
    for v in versenyzok:
        if v.rajtszam == rajtszam:
            return v
        
def lolenges():
    for v in versenyzok:
        if v.lolenges < 14.5:
            print(f'\t{v.nev}')

def statisztika():
    stat = {}
    for v in versenyzok:
        if v.orszag not in stat.keys():
            stat[v.orszag] = 1
        else:
            stat[v.orszag] += 1
    return stat
        
main()