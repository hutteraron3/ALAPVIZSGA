from dolgozo import Dolgozo

dolgozok_listaja: list[Dolgozo] = []

def load_from_file(filename: str) -> None:
    file = open(filename, 'r', encoding='utf-8')
    file.readline()
    for row in file:
        dolgozok_listaja.append(Dolgozo(row))
    file.close()

def uj_dolgozo_hozzaadasa(filename, uj_dolgozo) -> None:
    file = open(filename,'a', encoding='utf-8')
    file.write("\n" + uj_dolgozo)
        
        
    file.close()


def fizetes_hozzaadas(filename, uj_fizetes) -> None:
    file = open(filename,'a', encoding='utf-8')
    file.write(f';{uj_fizetes}')
        
        
    file.close()

def keres():
    legtobb = dolgozok_listaja[0]
    for p in dolgozok_listaja:
        if p.fizetes > legtobb.fizetes:
            legtobb = p
    return legtobb

def mentes(filename: str) -> None:
    file = open(filename, 'w', encoding='utf-8')
    file.write('Név;Új fizetése')
    for  p in dolgozok_listaja:
        print(p.nev + ";" + p.fizetes * 1.20)
    file.close()