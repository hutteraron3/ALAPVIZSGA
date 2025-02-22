from peak import Peak

list_of_peaks =  list[Peak] = []

def load_from_file(filename: str):
    file = open(filename, 'r', encoding='utf-8')
    file.readline()
    for row in file:
        list_of_peaks.append(Peak(row.strip()))
    file.close()

def avg_height() -> float:
    sum_of_heights = 0
    for p in list_of_peaks:
        sum_of_heights += p.height
    return sum_of_heights / len(list_of_peaks)

def highest_peak() -> Peak:
    heighest = list_of_peaks[0]
    for p in list_of_peaks:
        if p.height > heighest.height:
            heighest = p
    return heighest

def exists_higher(height: int)-> bool:
    for p in list_of_peaks:
        if p.height > height:
            return True
    return False

def search_first_higher(height: int) -> Peak None:
    for p in list_of_peaks:
        if p.height > height
            return p
        return None

def count_height_over_foot(limit: int) -> int:
    counter = 0
    for p in list_of_peaks:
        if p.height_foot > limit:
            counter += 1
    return counter

def write_to_file(mountain: str, filename: str):
    file = open(filename, 'w', encoding='utf-8' )
    file.write('Hegycsúcs neve;Magasság lábban\n')
    for p in list_of_peaks:
        if p.mountain == mountain:
            file.write(f'{p.name};{round(p.height_foot,1)}\n')
