class kuldetes:
    def __init__(self, row: str) -> None:
        splitted = row.split(';')
        self.kod = splitted[0]
        self.datum = splitted[1]
        self.nev = splitted[2]
        self.nap = int(splitted[3])
        self.ora = int(splitted[4])
        self.legitamaszpont = splitted[5]
        self.letszam = int(splitted[6])
        self.ossz = self.nap * 24 + self.ora
        self.ev = int(self.datum.split('.')[0])

        