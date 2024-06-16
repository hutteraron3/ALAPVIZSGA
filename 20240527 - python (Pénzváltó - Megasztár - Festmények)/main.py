from feladat3 import Festmeny

paintings : list[Festmeny] = []

def main():
    beolvas('paintings.txt')
    print(f'3.3 feladat: A fájlban tárolt festmények száma: {len(paintings)}')
    print(f'3.4 feladat: A Pablo Picasso képek száma: {Picasso("Pablo Picasso")} db')
    print(f'3.5 feladat: A legdrágább kép festője: {legdragabb().festo}, a kép címe: {legdragabb().festmeny}, becsült értéke: {legdragabb().becsult_ertek} dollár')
    if meghaladas() == True:
        print('3.6 feladat: Van olyan festmény, amelynek a becsült értéke nem haladja meg az eredeti árát.')
    if meghaladas() == False:
        print('3.6 feladat: Nincs olyan festmény, amelynek a becsült értéke nem haladja meg az eredeti árát.')

def beolvas(filename):
    file = open(filename, 'r', encoding='utf-8')
    file.readline()
    for row in file:
        paintings.append(Festmeny(row))

def Picasso(festo):
    counter = 0
    for p in paintings:
        if p.festo == festo:
            counter += 1
    return counter

def legdragabb():
    draga_as_fuck = paintings[0]
    for p in paintings:
        if draga_as_fuck.becsult_ertek < p.becsult_ertek:
            draga_as_fuck = p
    return draga_as_fuck

def meghaladas():
    for p in paintings:
        if p.eredeti_ar > p.becsult_ertek:
            return True
    else:
        return False
        


main()