# УЗОР (ВАРИАНТ 3)

WHITE = '\u001b[47m'
BLACK = '\u001b[40m'
END = '\u001b[0m'
print(f'{WHITE}{"  " * 6}{BLACK}{"  " * 2}{WHITE}{"  " * 6}{END}')
print(f'{BLACK}{"  " * 2}{WHITE}{"  " * 2}{BLACK}{"  " * 2}{WHITE}{"  " * 2}{BLACK}{"  " * 2}{WHITE}{"  " * 2}{BLACK}{"  " * 2}{END}')
print(f'{WHITE}{"  " * 2}{BLACK}{"  " * 2}{WHITE}{"  " * 6}{BLACK}{"  " * 2}{WHITE}{"  " * 2}{END}')
print(f'{BLACK}{"  " * 2}{WHITE}{"  " * 2}{BLACK}{"  " * 2}{WHITE}{"  " * 2}{BLACK}{"  " * 2}{WHITE}{"  " * 2}{BLACK}{"  " * 2}{END}')
print(f'{WHITE}{"  " * 6}{BLACK}{"  " * 2}{WHITE}{"  " * 6}{END}')




# ГРАФИК ФУНКЦИИ f(x) = 2 * x

plot_list = [[0 for i in range(10)] for i in range(10)]
result = [0 for i in range(10)]

for i in range(10):
    result[i] = i * 2

step = round(abs(result[0] - result[9]) / 9, 2)
print(step)

for i in range(10):
    for j in range(10):
        if j == 0:
            plot_list[i][j] = step * (8-i) + step

for i in range(9):
    for j in range(10):
        if abs(plot_list[i][0] - result[9 - j]) < step:
            for k in range(9):
                if 8 - k == j:
                    plot_list[i][k+1] = 1

for i in range(9):
    line = ''
    for j in range(10):
        if j == 0:
            line += '\t' + str(int(plot_list[i][j])) + '\t'
        if plot_list[i][j] == 0:
            line += '--'
        if plot_list[i][j] == 1:
            line += '/'
    print(line)
print('\t0\t1 2 3 4 5 6 7 8 9')


# ДИАГРАММА ПРОЦЕНТНОГО СООТНОШЕНИЯ(ВАРИАНТ 3)
# ЧИСЛА ОТ -3 ДО 3 И ОСТАЛЬНЫЕ


for i in range(10):
    #print(plot_list[i])
    pass

file = open('sequence.txt', 'r')
s = [float(x) for x in file]
s3 = [r for r in s if r >= -3.0 and r <= 3.0 ]

file.close()
print(s)
print(len(s3), len(s))
print((int(len(s3)) * 100) / int(len(s)), '% / 69.6 %')
BLUE = '\u001b[44m'
RED = '\u001b[41m'
for i in range(10):
    if i < 2:
        print(f'{BLUE}{"  " * 3}{RED}{"  " * 9}{END}')







