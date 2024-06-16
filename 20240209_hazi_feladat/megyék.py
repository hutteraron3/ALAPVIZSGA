from megye import Telepules

telepulesek_listaja: list[Telepules] = []

def load_from_file(filename: str):
    file = open(filename, 'r', encoding='utf-8')
    file.readline()
    for row in file:
        telepulesek_listaja.append(Telepules(row))
    
def how_many_people():
    people = 0
    for p in telepulesek_listaja:
        people += p.lakossag
    return people 

def smallest_village():
    smallest = telepulesek_listaja[0]
    for p in telepulesek_listaja:
        if p.terulet < smallest.terulet:
            smallest = p
    return smallest

def count(telepules_tipus: str) -> int:
    count = 0
    for p in telepulesek_listaja:
        if p.rang == telepules_tipus:
            count += 1
    print(count)

def write_file(filename: str, telepules_tipus):
    file = open(filename, 'w', encoding='utf-8')
    file.write('Település,Rang,Térség,Terület,Lakosság')
    for p in telepulesek_listaja:
        if p.rang == telepules_tipus:
            file.write(f'\n{p.telepules},{p.rang},{p.terseg},{p.terulet},{p.lakossag}')