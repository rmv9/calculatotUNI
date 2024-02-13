from time import sleep as s


def animate_infinity(char, flag=True, temp=1):

    while flag:
        print(char, end=''), s(temp)
        print('\r', end=''), s(temp)


def do_tele_matrix(matrix, temp=.8):

    for row in matrix:
        for element in row:
            print(element, end=' '), s(temp)
        print()


def do_tele_cycle_words(text, separate=' ', temp=.8):

    for w in text.split(separate):
        print(w), s(temp)


def do_tele_chars(text, temp=.3):

    for c in str(text):
        print(c, end=''), s(temp)
    return '\n'


def do_tele_chars_and_rev(text, temp=.3):

    text = str(text).strip()
    for c in str(text):
        print(c, end=''), s(temp)
    for i in range(1):
        print('*' * (i + 1), end='\r'), s(temp)
    for i in range(1, len(str(text)) + 2):
        print(text, end=''), s(temp)
        print('\r', end='')
        text = text[0:len(str(text)) - 1]


def do_tele_char_darts(text, dart_cnt=4, temp=.3):

    for c in text:
        print(c, end=''), s(temp)
    for _ in range(dart_cnt):
        print('.', end='')
        s(temp)


def do_tele_math(n1, n2, ans, opr, temp=.4):

    for c in (n1, opr, n2, '=', ans):
        print(c, end=' '), s(temp)


def do_tele_words(text: str, temp=.5):

    for w in (text.split()):
        print(w, end=' '), s(temp)


def animate_reverse(text, temp=.3):

    text = text.strip()
    for i in range(1, len(str(text)) + 2):
        print(text, end=''), s(temp)
        print('\r', end='')
        text = text[0:len(text) - 1]


def animate_words_del(text: str, temp=.5):

    for w in (text.split()):
        print(w, end=' '), s(temp)
    for i in range(1):
        print('*' * (i + 1), end='\r'), s(temp)


def animate_chars_del(text, temp=.3):

    for c in str(text):
        print(c, end=''), s(temp)
    for i in range(1):
        print('*' * (i + 1), end='\r'), s(temp)


def clear(sec=.3):

    for i in range(1):
        print('*' * (i + 1), end='\r'), s(sec)