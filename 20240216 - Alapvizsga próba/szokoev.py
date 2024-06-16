def szokoev(ev) -> bool:
    if ev % 400 == 0:
        return True
    if ev % 4 == 0 and ev % 100 != 0:
        return True
    return False


print('2. feladat: Szökőév listázó')
ev1 = int(input('Kérem az egyik évszámot: '))
ev2 = int(input('Kérem a másik évszámot: '))

if ev1 > ev2:
    ev1, ev2 = ev2, ev1

szokoevek = []
for i in range(ev1, ev2+1):
    if szokoev(i):
        szokoevek.append(i)

if len(szokoevek) == 0:
    print('Nincs szökőév a megadott tartományban!')
else:
    print('Szökőévek:', end=' ')
    print(szokoevek)

