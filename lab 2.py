# генератор ссылок
# для файла 'books'
from csv import reader
file = open('t.txt', 'w')
with open('books.csv', 'r') as csvfile:

    table = reader(csvfile, delimiter=';')
    pp = []
    for row in list(table)[1:21]:
        author = row[3]
        title = row[1]
        year = row[6]
        a = f'{author}. {title} - {year}'
        pp.append(a)
    for x, y in enumerate(pp, start=1):
        file.write(f'{x}. {y}\n')
file.close()