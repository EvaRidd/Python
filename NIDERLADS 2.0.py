RED = '\u001b[41m'
BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
END = '\u001b[0m'
print(u"\u001b[34;1m  Н \u001b[31;1m И \u001b[32;1m Д \u001b[33;1m Е \u001b[0m Р \u001b[31;1m Л \u001b[35;1m А \u001b[34;1m Н \u001b[32;1m Д \u001b[31;1m Ы \u001b[33;1m")
for i in range(2):

    if i < 1:
        print(f'{END}')
    else:
        print(f'{RED}{"  " * 10}{END}')
        print(f'{WHITE}{"  " * 10}{END}')
        print(f'{BLUE}{"  " * 10}{END}')
