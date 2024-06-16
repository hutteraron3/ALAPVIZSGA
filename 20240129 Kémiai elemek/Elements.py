from Element import Element


elements : list[Element] = []

def load_from_file(filename: str) -> None:
    file = open(filename, 'r', encoding='utf-8')
    file.readline()
    for row in file:
        elements.append(Element(row))
    file.close()
