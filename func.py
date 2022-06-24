def pr(text):
    print('Длина текста равна = ', len(text))
    print(text.upper())
    print('=' * 30)
    print('!!!', __name__)


def pr1(text):
    print()
    print('Вы только что уcпешно ввели следующий текст: \n', text)
    print('Длина Вашего текста составляет ', len(text), 'символов')


def pr3(text):
    print('А вот квадрат длины Вашего текста составляет:')
    print(len(text)**2)
    print('='*40)