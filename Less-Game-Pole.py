# text = '''
# Парагвайская «Олимпия» не погасит долг перед киевским «Динамо» по трансферу Дерлиса Гонсалеса до пятницы, как это предусматривает предписание.
#
# Об этом заявил член директивной комиссии клуба Педро Балотта, отметивший, что «Олимпию» теперь ожидают санкции.
#
# «У нас нет денег. Долги не выплачиваются, потому что мы этого не хотим. Речь о больших деньгах, которые нужно вкладывать, это не просто так. Долг по Дерлису Гонсалесу не будет выплачен, потому что денег нет. Надо работать, чтобы были», - цитирует Балотту D10.
#
# Вероятнее всего, ФИФА поначалу запретит «Олимпии» регистрировать новых футболистов, однако со временем, если долг так и не будет погашен, может ужесточить санкции.
#
# Напомним, «Олимпия» должна «Динамо» 5 миллионов долларов за Дерлиса Гонсалеса и еще 0,5 миллиона в виде штрафных санкций и судебных издержек, так как парагвайский клуб не признавал долг и дело дошло до Спортивного арбитража Лозанны.
# '''
# t = []
# for i in text:
#     if i.isalpha() or i == ' ':
#         t.append(i)
# text = ''.join(t)
#
# text = list(set(text.upper().split()))
# print(text)


import random


def inp_secret_word():
    text = ['ЕСЛИ', 'ДОЛГ', 'ЭТО', 'ДЕНЬГИ', 'ДЕЛО', 'ЕЩЕ', 'МЫ', 'НАДО', 'ТАК', 'ВИД', 'ОЛИМПИЯ', 'МИЛЛИОН']
    secret_word = random.choice(text)
    # Validation or choose from list
    return secret_word

# print(inp_secret_word())


def calc_attempts(secret_word):
    attempts = len(secret_word)
    return attempts
#

# word1 = list('_' * len(secret_word))
word1 = list('_____________')
print(*word1)
# word1[2] = 'A'
# word1[4] = 'K'
# if attempts < 1 or word1.count('_') == 0:
#
# print(*word1)




def write_word(secret_word, symbol, word):
    for i in range(len(secret_word)):
        if symbol == secret_word[i]:
            word[i] = symbol
    pass
    # в______е
#
def screen(word, lst_letters, attempts):
    print()
    print()
    print(*word)
    print('У Вас осталось ', attempts, 'попыток.')
    print('Вы уже испольовали следующие буквы :', *lst_letters)
    pass
#
def inp_symbol():
    symbol = input()
    # Validation
    return symbol
#
#
def check_game(word, attempts):
    pass
    # if .... :
    #     result = '....'
    # return result
#
#




def run_game():

    secret_word = inp_secret_word()
    attempts = calc_attempts(secret_word)
    my_symb = '_'
    word = list(my_symb * attempts)
    while my_symb in word and attempts:
        symbol = inp_symbol()
        write_word()
    if my_symb in word:
        print('Game over')
    else:
        print('Win')


#     #
#     #
#     #
#     #
#     #

    pass
#


run_game()