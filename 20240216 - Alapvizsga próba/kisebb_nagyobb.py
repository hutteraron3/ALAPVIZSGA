print('1. feladat: Kisebb-nagyobb meghatározása')
szam1 = int(input('Kérem az első számot: '))
szam2 = int(input('Kérem a második számot: '))

if szam1 > szam2:
    print(f'A nagyobb szám {szam1} a kisebb {szam2}')
elif szam2 > szam1:
    print(f'A nagyobb szám {szam2} a kisebb {szam1}')
else:
    print('A két szám egyenlő.')

