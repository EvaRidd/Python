# генератор ссылок
# для файла 'books'
from csv import reader
file = open('books.txt', 'w+')
with open('books.csv', 'r') as csvfile:

    table = reader(csvfile, delimiter=';')
    pp = []
    for row in list(table)[1:21]:

        a = [row[1], row[3], row[6]]
        pp.append(a)
    for x, y in enumerate(pp, start=1):
        file.write(f'{x}:{y}')
file.close()

# для файла 'books-en'
file = open('list.txt', 'w+')
with open('books-en.csv', 'r') as csvfile:

    table = reader(csvfile, delimiter=';')
    pp = []
    for row in list(table)[1:21]:

        a = [row[1], row[3], row[6]]
        pp.append(a)
    for x, y in enumerate(pp, start=1):
        file.write(f'{x}:{y}')
file.close()
