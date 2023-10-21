# генератор ссылок
from csv import reader
with open('books.csv', 'r') as csvfile:
    table = reader(csvfile, delimiter=';')
    pp = []
    for row in list(table)[1:21]:

        a = [row[1], row[3], row[6]]
        pp.append(a)
    for x, y in enumerate(pp, start=1):
        print(f'{x}:{y}')


from csv import reader
with open('books-en.csv', 'r') as csvfile:
    table = reader(csvfile, delimiter=';')
    pp = []
    for row in list(table)[1:21]:

        a = [row[1], row[2], row[3]]
        pp.append(a)
    for x, y in enumerate(pp, start=1):
        print(f'{x}:{y}')
