class Result:
    def __init__(self, row) -> None:
        splitted = row.split(' ')
        self.place = int(splitted[0])
        self.members = int(splitted[1])
        self.sport = splitted[2]
        self.category = splitted [3]

        match self.place:
            case 1:
                self.points = 7
                self.points = 6
                self.points = 5
                self.points = 4
                self.points = 3
                self.points = 2
                self.points = 1
