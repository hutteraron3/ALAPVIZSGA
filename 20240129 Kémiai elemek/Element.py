class Element:
    def __init__(self, row: str) -> None:
        splitted = row.split(';')
        self.age = splitted[0]
        self.name = splitted[1]
        self.vegyjel = splitted[2]
        self.number = splitted[3]
        self.creator = splitted[4]
        