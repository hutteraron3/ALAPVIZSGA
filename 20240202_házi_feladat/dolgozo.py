class Dolgozo:
    def __init__(self, row: int) -> None:
        splitted = row.strip().split(';')
        self.nev = splitted[0]
        self.fizetes = int(splitted[1])