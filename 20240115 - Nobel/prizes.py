from prize import Prize

nobel_prizes : list[Prize] = []

def load_from_file(filename: str) -> None:
    file = open(filename, 'r', encoding='utf-8')
    file.readline()
    for row in file:
        new_prize = Prize(row.strip())
        nobel_prizes.append(new_prize)
    file.close()

def print_all_names():
    for p in nobel_prizes:
        print(p.last_name)

def search_by_name(name: str) -> Prize|None:
    for p in nobel_prizes:
        if p.full_name == name:
            return p
    return None

def search_by_year_and_type(year: int, type: str) -> Prize|None:
    for p in nobel_prizes:
        if p.year == year and p.type == type:
            return p
    return None

def search_organization_by_type_from(type: str, year_from: int) -> list[Prize]:
    result: list[Prize] = []
    for p in nobel_prizes:
        if p.type == type and p.year >= year_from and p.last_name == '':
            result.append(p)
    return result