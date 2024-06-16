class Kuldetes:
    def __init__(self, row) -> None:
        stripped = row.split(';') # strip() levágja a szóközöket
        self.kod = stripped[0]
        self.datum = stripped[1]
        self.nev = stripped[2]
        self.nap = int(stripped[3])
        self.ora = int(stripped[4])
        self.legitamasz = stripped[5]
        self.letszam = int(stripped[6])
        self.osszes = self.nap * 24 + self.ora
        self.ev = self.datum.split(',')[0]