# вариант 3
# словарь вида {'название предмета':(ячейки, очки выживания) }
stuffdict = {
    'r': (3, 25),
    'p': (2, 15),
    'a': (2, 15),
    'm': (2, 20),
    'i': (1, 5),
    'k': (1, 15),
    'x': (3, 20),
    't': (1, 25),
    'f': (3, 15),
    'd': (1, 10),
    's': (2, 20),
    'c': (2, 20),
}

# 2x4 вывод
bag = [['-' for i in range(4)] for x in range(2)]

# Функция для расчета общих очков выживания в рюкзаке
def calculate_survival_points(bag):
    total_points = 10
    for x in bag:
        for item in x:
            if item != '-':
                total_points += stuffdict[item][1] # Получаем очки выживания из словаря
    return total_points

# Функция для поиска наиболее подходящего предмета для размещения в ячейке рюкзака
def find_best_item(bag, available_items):
    best_item = 0
    max_points = 0
    for item in available_items:
        if item == 'd': #Том заражён значит предмет d должен обязательно быть в рюкзаке
            return item
        elif stuffdict[item][1] > max_points:
            max_points = stuffdict[item][1]
            best_item = item
    return best_item

# Размещаем предметы в ячейках рюкзака
available_items = list(stuffdict.keys())
for x in bag:
    for i in range(4):
        if len(available_items) == 0:
            break
        best_item = find_best_item(bag, available_items)
        if best_item != 0:
            x[i] = best_item
            available_items.remove(best_item)

for x in bag:
    print(x)
print("Общие очки выживания:", calculate_survival_points(bag))