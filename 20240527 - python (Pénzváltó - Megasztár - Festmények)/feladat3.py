class Festmeny:
    def __init__(self, row) -> None:
        splitted = row.strip().split(';')
        self.festmeny = splitted[0]
        self.festo = splitted[1]
        self.keszites_eve = int(splitted[2])
        self.becsult_ertek = int(splitted[3])
        self.eredeti_ar = int(splitted[4])
        self.eladas_eve = int(splitted[5])

