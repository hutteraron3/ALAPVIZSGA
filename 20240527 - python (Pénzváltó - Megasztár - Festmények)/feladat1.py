penznem = str(input('Eurót (EUR) vagy forintot (HUF) akarsz váltani? '))
if penznem == 'EUR':
    n = int(input('Hány eurót akarsz beváltani? '))
    print(f'{n} euróért {n * 365} forintot kapsz.')
if penznem == 'HUF':
    h = int(input('Hány forintot akarsz beváltani? '))
    print(f'{h} forintért {round(h / 365, 2)} eurót kapsz.')

