from toto import Toto

toto_lista : list[Toto] = []

def main():
    beolvas('toto.txt')
    print('3. feladat: Toto')
    print('3.1 feladat: Adatok beolvasása és tárolása')
    print(f'3.2 feladat: Fogadási fordulók száma: {len(toto_lista)}')
    print(f'3.3 feladat: Telitalálatos szelvények száma: {telitalatos_szelvenyek()} darab')
    if dontetlen_merkozes() == False:
        print(f'3.4 feladat: Nem volt döntetlen mentes forduló!')
    if dontetlen_merkozes() == True:
        print(f'3.4 feladat: Volt döntetlen mentes forduló!')



def beolvas(filename):
    file = open(filename, 'r', encoding='utf-8')
    file.readline()
    for row in file:
        toto_lista.append(Toto(row))

def telitalatos_szelvenyek():
    counter = 0
    for t in toto_lista:
        counter += t.telitalalat
    return counter

def dontetlen_merkozes():
    for t in toto_lista:
        if 'X' not in t.eredmenyek:
            return True   
    return False
             
main()