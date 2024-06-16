from prizes import *

load_from_file('nobel.csv')
# print_all_names()
result = search_by_name('Arthur B. McDonald')
if result == None:
    print('Nincs ilyen néven díjazott.')
else:
    print(f'Arthur B. McDonald {result.type} díjat kapott.')

result = search_by_year_and_type(2017, 'irodalmi')
if result == None:
    print('2017 évben nincs irodalmi díjazott.')
else:
    print(f'2017-ben irodalmi Nobel-díjatt kapott: {result.full_name}')

print('1990 után béke Nóbel-díjat kaptak az alábbi szervezetek:')
for p in search_organization_by_type_from('béke', 1990):
    print(f'\t{p.first_name}')
