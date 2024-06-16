class Telepules:
    def __init__(self, row) -> None:
        splitted = row.strip().split(',')
        self.telepules = splitted[0]
        self.rang = splitted[1]
        self.terseg = splitted[2]
        self.terulet = int(splitted[3])
        self.lakossag = int(splitted[4])