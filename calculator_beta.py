
import datetime, time, text, sys, locale  
from time import sleep as s
import teleprint_calc as anim  
import script_func as sf  

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

# contains the result-strings of all operations, list of error-logs
logs = []  
troubles = [] 

main_date = datetime.datetime.now()  # reading and save system date/time as main_date
cur_time = main_date.strftime('%H:%M')  # string in format HH:MM
cur_date = main_date.strftime('%d.%m.%Y')  # date in str format dd.mm.yyyy
start_time = time.monotonic()

sf.file_open_wr(main_date)  # writing time and date status in default txt.file (history.txt)

sys.stdout.write('\n'+text.prog_name.capitalize()), s(1.5)  # title line. Write and delete name of program
sys.stdout.write('\r'), s(.3)  # delete previous line
anim.do_tele_chars(text.ver), s(1), anim.clear()  # animated version of prog and delete script clear()
sf.date_time_status(main_date, cur_time)  # print date and time status

while True:  # main cycle
    print('\n')  # todo change input() to sys.stdin
    user_num_1 = float(sf.user_num_1())  # input first number
    operator_1 = sf.operator_1()  # operator
    user_num_2 = float(sf.user_num_2(operator_1))

    result, outro = sf.main_proc(user_num_1, user_num_2, operator_1) 

    anim.do_tele_words(outro.capitalize()), s(.7), anim.clear()
    anim.do_tele_chars_and_rev(round(result), .2)
    anim.do_tele_math(user_num_1, user_num_2, round(result, 4), operator_1, .3), s(.5)
    anim.do_tele_chars('-> ', .3), anim.do_tele_chars(round(result)), print()

    logs.append(sf.logs_list_saver(user_num_1, user_num_2, operator_1, round(result, 4)))

    s(1), anim.do_tele_cycle_words('\n1-выход', ' ', .5)
    if input('->') == '1':
        break

sys.stdout.write('\nИстория\n'), s(.5)
sf.do_logs_print(logs)
finish_time = time.monotonic()
session_time = finish_time - start_time
sf.time_marker_converter(session_time)
sf.file_close_wr(logs, troubles, cur_time, session_time)
