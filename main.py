import csv




RED = '\x1b[41m'
WHITE = '\x1b[47m'
END = '\x1b[0m'



print('\033[0;31;41m' + "0" * 5 + '\033[0;0m')
print('\033[0;31;41m' + "0" * 2 + '\033[0;37;47m' + "0" * 1 + '\033[0;31;41m' + "0" * 2 + '\033[0;0m')
print('\033[0;31;41m' + "0" * 1 + '\033[0;37;47m' + "0" * 3 + '\033[0;31;41m' + "0" * 1 + '\033[0;0m')
print('\033[0;31;41m' + "0" * 2 + '\033[0;37;47m' + "0" * 1 + '\033[0;31;41m' + "0" * 2 + '\033[0;0m')
print('\033[0;31;41m' + "0" * 5 + '\033[0;0m')


print("")


print(f"{WHITE}   {RED}     {WHITE}   {RED}     {WHITE}   {END}")
print(f"{WHITE}  {RED}  {WHITE}   {RED}  {WHITE} {RED}  {WHITE}   {RED}  {WHITE}  {END}")
print(f"{WHITE} {RED}  {WHITE}     {RED}   {WHITE}     {RED}  {WHITE} {END}")
print(f"{WHITE} {RED} {WHITE}       {RED} {WHITE}       {RED} {WHITE} {END}")
print(f"{WHITE} {RED} {WHITE}       {RED} {WHITE}       {RED} {WHITE} {END}")
print(f"{WHITE} {RED}  {WHITE}     {RED}   {WHITE}     {RED}  {WHITE} {END}")
print(f"{WHITE}  {RED}  {WHITE}   {RED}  {WHITE} {RED}  {WHITE}   {RED}  {WHITE}  {END}")
print(f"{WHITE}   {RED}     {WHITE}   {RED}     {WHITE}   {END}")








def in_1(in1, st1):
    for i in range(10):
        for j in range(10):
            if j == 0:
                in1[i][j] = round(st1 * (9 - i), 1)
            if i == 9:
                in1[i][j] = j
    return in1


def fill(f, res, st):
    for i in range(9):
        for j in range(10):
            if abs(f[i][0] - res[9-j]) < st:
                for k in range(9):
                    if 8 - k == j:
                        f[i][k + 1] = 1
    return f


def draw_plot(array_pl):
    for i in range(9):
        line = ''
        for j in range(10):
            if j == 0:
                line += WHITE + str(array_pl[i][j]) + '\t'
            if array_pl[i][j] == 0:
                line += '  '
            if array_pl[i][j] == 1:
                line += RED + '  ' + WHITE
        line += END
        print(line)
    print(f'{WHITE}  0  1 2 3 4 5 6 7 8 9 {END}')




array_plot = [[0 for col in range(10)] for row in range(10)]
result = [0 for col in range(10)]
for i in range(10):
    result[i] = round(i/3, 1)


step = round(abs(result[9] - result[0]) / 9, 1)
print(step)

in_1(array_plot, step)
fill(array_plot, result, step)
draw_plot(array_plot)



s = 0
other = 0

with open('books.csv') as f:
    reader = csv.DictReader(f, delimiter=';')
    for row in reader:
        if "16" == row.get("Возрастное ограничение на книгу"):
            s += 1
        else:
            other += 1

print('Книги для возраста 16 лет')
print(RED + ' ' * int(s / (other + s) * 100) + WHITE + str(
    int(s / (other + s) * 100)) + "%" +  END)
print('Остальные книги')
print(RED + ' ' * int(other / (other + s) * 100) + WHITE + str(
    100 - int(s / (other + s) * 100)) + "%" + END)








