import teleprint_calc as anim
from time import sleep as s
import text
import sys


#  returns time mark
def time_marker_converter(mono_time: int) -> str:
    """
    signature require monotonic or seconds time values
    """
    hours = round((mono_time / 60) / 60)
    minutes = round(mono_time / 60)
    seconds = round(mono_time % 60)
    return f'Session time: {hours} hrs. {minutes} min. {seconds} sec.'


def file_open_wr(date) -> str:
    """
    arg is datetime.datetime only
    writed time and data status in default file
    """
    cur_time = date.strftime('%H:%M')
    cur_date = date.strftime('%d.%m.%Y')

    with open('history.txt', 'a', encoding='utf-8') as file:
        file.writelines(f'START DATE {cur_date}\ntime: {cur_time}, ({date.strftime('%B')}) \n')
        file.writelines('_\n')
    file.close()

    return 'file updated'


def file_close_wr(list_1, list_2, time, session_time):
    """
    writes logs in .txt before exit
    """
    with open('history.txt', 'a', encoding='utf-8') as file:
        file.writelines(f'FINISH DATE (записано в {time}):\n')
        [file.writelines(f'{i}) {list_1[i - 1]}\n') for i in range(1, len(list_1) + 1)]
        file.writelines(f'Время сессии: {round(session_time/60)} мин. {round(session_time)%60} сек.\n')
        file.write('\n')
        if len(list_2):
            file.writelines('Невыполненные запросы:\n')
            [file.writelines(f'{i}) {list_2[i - 1]}') for i in range(1, len(list_2) + 1)]
        file.writelines('___________________\n')


def file_err_writer(description='n/n'):
    """
    write problems in the defoult file 
    """
    with open('history.txt', 'a', encoding='utf=8') as file:
        file.writelines('----\n')
        file.writelines(f'(!) {text.input_incor} ({description})\n')
        file.writelines('----\n')
    return sys.stdout.write('save status'), s(1.5), sys.stdout.write('\r')


def date_time_status(today, time, temp=.5):
    """
    'time' must be .strftime(%H:%M) format only
    arg 'today' is datetime.now()
    """
    months = {1: 'января', 2: 'февраля', 3: 'марта',
              4: 'апреля', 5: 'мая', 6: 'июня',
              7: 'июля', 8: 'августа', 9: 'сентября',
              10: 'октября', 11: 'ноября', 12: 'декабря'}

    days = {1: 'понедельник',
            2: 'вторник',
            3: 'среда',
            4: 'четверг',
            5: 'пятница',
            6: 'суббота',
            7: 'воскресенье'}

    time = time.split(':')

    if int(time[0]) in range(4, 11):
        time = 'Доброе утро'
    elif int(time[0]) in range(11, 17):
        time = 'Добрый день'
    elif int(time[0]) in range(17, 24):
        time = 'Добрый вечер'
    elif int(time[0]) in range(4):
        time = 'Доброй ночи'

    return (sys.stdout.write(f'{time}!\n'), s(temp),
            sys.stdout.write(f'{days[today.isoweekday()].capitalize()}, '), s(temp),
            sys.stdout.write(f'{str(today.day)} {months[today.month]}')), s(temp)


def logs_list_saver(num1, num2, opr, answer) -> str:
    """
    reformat args -> string
    """
    return f'{num1} {opr} {num2} = {answer}'


def do_logs_print(lst: list, temp=(.3)):
    """
    animated print
    """
    for i in range(len(lst)):
        print(str(i + 1) + '.', lst[i], end='\n'), s(temp)


def main_proc(num1: float, num2: float, operator: str):

    match operator:
        case '+':
            return num1 + num2, text.sum_txt
        case '-':
            return num1 - num2, text.dif_txt
        case '*':
            return num1 * num2, text.prod_txt
        case '/':
            return num1 / num2, text.quot_txt
    
    raise ValueError('Unexpected operator')


def user_num_1() -> float:
    """
    user-input filter
    Decimal rebuild needed 
    """
    while True:
        anim.do_tele_words(text.inp_txt_1.capitalize(), .3)
        try:
            number = float(input().strip().replace(',', '.'))
        except ValueError:
            print(), anim.animate_words_del(text.input_incor.capitalize())
            file_err_writer('num_1/ValueError')
            continue
        if len(str(number)) > 15:
            print(), anim.animate_words_del(text.lim_incor.capitalize())
            file_err_writer('num_1/out of limit')
        else:
            return number


def operator_1() -> str:

    while True:
        anim.do_tele_words(text.inp_oper.capitalize(), .3)
        char = input().strip()
        if char in text.operators:
            return char
        else:
            print(), anim.animate_words_del(text.input_incor)
            file_err_writer('operator')


def user_num_2(operator: str) -> float:

    while True:
        anim.do_tele_words(text.inp_txt_2.capitalize(), .3)
        try:
            number = float(input().strip().replace(',', '.'))
        except ValueError:
            print(), s(.4), anim.animate_words_del(text.input_incor.capitalize())
            continue
        if len(str(number)) > 15:
            print(), s(.4), anim.animate_words_del(text.lim_incor)
            with open('history.txt', 'a', encoding='utf=8') as file:
                file.writelines('----\n')
                file.writelines(f'(!) {text.input_incor} (размерность числа)\n')
                file.writelines('----\n')
        elif not number and operator == text.operators[-1]:
            print(), s(.5), anim.animate_words_del(text.zero_incor)
            with open('history.txt', 'a', encoding='utf=8') as file:
                file.writelines('----\n')
                file.writelines(f'(!) {text.input_incor} (деление на ноль)\n')
                file.writelines('----\n')
        else:
            return number
