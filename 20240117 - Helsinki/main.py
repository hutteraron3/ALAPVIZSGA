from Helsinki import *

load_from_file('helsinki.txt')
print('3. feladat')
print(f'Pontszerző helyezések száma: {len(results)}')
print('4. feladat')
print(f'Arany: {count_places(1)}')
print(f'Ezüst: {count_places(2)}')
print(f'Bronz: {count_places(3)}')
print(f'Összesen: {count_places(1)+count_places(2)+count_places(3)}')
print('5. feladat')
print(f'Olimpiai pontok összesen: {sum_points()}')
print('6. feladat')
torna = count_by_sport('torna')
uszas = count_by_sport('uszas')

if torna > uszas:
    print('Több érmet szereztek tornában.')
elif uszas > torna:
    print('Több érmet szereztek úszásban.')
else:
    print('Egyenlő.')

write_to_file('helsinki2.txt')

most = most_members()
print('8. feladat')
print(f'Helyezés: {most.place}')
print(f'Sportág: {most.sport}')
print(f'Versenyszám: {most.category}')
print(f'Sportolók száma: {most.}')