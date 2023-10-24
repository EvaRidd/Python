# количество записей, у которых в поле Название строка длиннее 30 символов
from csv import reader
a = []
with open('books.csv', 'r') as csvfile:
    table = reader(csvfile, delimiter=';')
    for row in table:
        if len(str(row[1])) > 30:
            a.append(row[1])
print(len(a))


# для файла 'books-en'
a = []
with open('books-en.csv', 'r') as csvfile:
    table = reader(csvfile, delimiter=';')
    for row in table:
        if len(str(row[1])) > 30:
            a.append(row[1])
print(len(a))
# для файла 'books'
#  поиск книги по автору(3 вариант)
flag = 0
search = input('search for:')

with open('books.csv', 'r') as csvfile:
    table = reader(csvfile, delimiter=';')
    for row in list(table):
        lower_case = row[3].lower()
        index = lower_case.find(search)
        if index != -1:
            if '2014' in str(row[6]) or '2016' in str(row[6]) or '2017' in str(row[6]):
                print(row[1])
                flag = 1
    if flag == 0:
        print('Nothing found')



















