from megyék import *

def main():
    load_from_file('szszb.csv')
    print(f'3. feladat: Települések száma: {len(telepulesek_listaja)}')
    print(f'4. feladat: A megye lakossága: {how_many_people()} fő')
    smallest = smallest_village()
    print(f'5. feladat: A legkisebb területű település:')
    print(f'Település neve: {smallest.telepules}')
    print(f'Területe: {smallest.terulet} ha')
    print(f'6. feladat: A megyében: ennyi nagyközség található: {count("nagyközség")}')
    write_file('varosok.csv', 'város')

    
main()