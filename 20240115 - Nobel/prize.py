class Prize:
    def __init__(self, row: str) -> None:
        splitted = row.split(';')
        # év;típus;keresztnév;vezetéknév
        self.year = int(splitted[0])
        self.type = splitted[1]
        self.first_name = splitted[2]
        self.last_name = splitted[3]

        self.full_name = self.first_name + ' ' + self.last_name