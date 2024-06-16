from peaks import *

def main():
    load_from_file('hegyekMo.txt')
    print(f'3. feladat: Hegycsúcsok száma: {len(list_of_peaks)} darab')
    print(f'4. feladat: Hegycsúcsok átlagos magassága: {avg_height()}m')
    print('A legmagasabb hegycsúcs adatai: ')
    highest = highest_peak()
    print(f'\tNév: {highest.name}')
    print(f'\tHegység: {highest.mountain}')
    print(f'\tMagasság: {highest.height}')
    height = int(input('6. feladat: Kérek egy magasságot: '))
    if exists_higher(height):
        print(f'\tVan {height} méternél magasabb hegycsúcs.')
    else:
        print(f'\tVan {height} méternél magasabb hegycsúcs.')


    search_result = search_first_higher(height)
    if search_result != None:
        print(f'\tVan {height} méternél magasabb hegycsúcs,például: {search_result.name}')
    else:
        print(f'\tVan {height} méternél magasabb hegycsúcs.')

    print(f'7. feladat: 3000 lábnál magasabb hegycsúcsok száma: {count_height_over_foot}')

    print(f'9. feladat: bukk-videk.txt')
    
main()