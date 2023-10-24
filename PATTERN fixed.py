file = open('sequence.txt', 'r')
s = [float(x) for x in file]
s3 = [r for r in s if r >= -3.0 and r <= 3.0 ]

file.close()
print(s)
print(len(s3), len(s))
print((int(len(s3)) * 100) / int(len(s)), '% /', 100 - (int(len(s3)) * 100) / int(len(s)),'%')
BLUE = '\u001b[44m'
RED = '\u001b[41m'
END = '\u001b[0m'
a = int(((int(len(s3)) * 100) / int(len(s)))/10)
b = int((100 - (int(len(s3)) * 100) / int(len(s)))/10)
for i in range(8):
    if i < 2:
        print(f'{BLUE}{"  " * a}{RED}{"  " * b}{END}')
