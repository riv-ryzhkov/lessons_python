def game(sp):
    for i in range(3):
        print(*sp[i])


def valid(s):
    if len(s) != 3 or s[1] != " " or not s[0].isdigit() or not s[2].isdigit():
        game(sp)
        print('=' * 80)
        print('Nekorrektnye koordinaty, try again. ')
        return False
    a = int(s[0])
    b = int(s[2])
    if a < 1 or a > 3 or b < 1 or b > 3:
        game(sp)
        print('=' * 80)
        print('Net takoi stroki / stolbtsa. Vvedite chisla ot 1 do 3')
        return False
    if sp[a - 1][b - 1] != '.':
        game(sp)
        print('=' * 80)
        print('Mesto zanyato. Vvedite drugoi hod!')
        return False
    return True


def step(sp, pl) -> object:
    while True:
        print('=' * 80)
        s = input('Vvedite koordinaty cherez probel: ')
        if valid(s):
            s = s.split()
        else:
            continue
        if pl == 1:
            sp[int(s[0]) - 1][int(s[1]) - 1] = 'x'
        else:
            sp[int(s[0]) - 1][int(s[1]) - 1] = '0'
        return sp


def check(l):
    for k in ['x', '0']:
        for i in range(3):
            if l[i][0] == l[i][1] == l[i][2] == k or l[0][i] == l[1][i] == l[2][i] == k:
                return True
        if l[0][0] == l[1][1] == l[2][2] == k or l[0][2] == l[1][1] == l[2][0] == k:
            return True
    return False


sp = []
for i in range(3):
    sp.append(['.', '.', '.'])
pl = -1
vin = False
while vin == False:
    sum = 0
    for i in range(3):
        sum += sp[i].count('.')
    if sum == 0:
        pl = 0
    if check(sp) or pl == 0:
        vin = True
        break
    pl *= -1
    game(sp)
    if pl == 1:
        print('PLAYER ("х")')
    else:
        print('PLAYER ("0")')
    step(sp, pl)

print('=' * 40)
if pl == 1:
    print('Победил 1й игрок ("х")')
elif pl == 0:
    print('Поздравляю! Ничья!')
else:
    print('Победил 2й игрок ("нолик")')
print('=' * 40)
game(sp)
