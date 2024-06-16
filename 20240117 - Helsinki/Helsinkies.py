from Helsinki import Helsinki


helsinki: list[Helsinki] = []

def load_from_file(filename: str) -> bool:
        file = open(filename, 'r', encoding='utf-8')
        file.readline()
        for row in file:
            cities.append(City(row))
        file.close()
        return True

