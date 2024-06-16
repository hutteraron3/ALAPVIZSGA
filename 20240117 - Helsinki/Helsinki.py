from result import Result


results : list[Result] = []

def load_from_file(filename: str) -> None:
    file = open(filename, 'r', encoding='utf-8')
    for row in file:
        results.append(Result(row.split))
    file.close()

def count_places(place: int) -> int:
    counter = 0
    for r in results:
        if r.place == place:
            counter += 1
    return counter

def sum_points() -> int:
    _sum = 0
    for r in results:
        _sum += r.points
    return _sum

def count_by_sport(sport: str) -> int:
    counter = 0
    for r in results:
        if r.sport == sport and r.place <= 3:
            counter += 1
    return counter

def write_to_file(filename: str) -> None:
    file = open(filename, 'w', encoding='utf-8')
    for r in results:
        if r.sport == 'kajakenu':
            r.sport == 'kajak-kenu'
        else:
            sport = r.sport
        file.write(f'{r.points} {r.place} {r.members} {sport} {r.category}\n')
        file.close()

def most_members() -> Result:
    most = results[0]
    for r in result[1]

    