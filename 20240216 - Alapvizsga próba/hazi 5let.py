self.matek = str_to_list(splitted[2])

def str_to_list(self, str):
    lista = []
    s = str.split(',')
    for x in s:
        lista.append(x)
    return lista