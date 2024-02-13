# python
# rmv9
# CALCULATOR_BETA v.1
# copy_past line

# update list

# float and minus (-7, -14, -0.5) operands added                        1.11
# round answer numbers                                                  1.12
# number.strip() method                                                 1.13
# convert lists to dictionary
# change cycles user_number_1 -> cycle_num_1 or else
# debug space-inter error                                               1.14
# txt_list pack added
# animated intro added                                                  1.15
#
# todo list
# 1. dev interface
# 2. add list modul backend
# 3. add math module backend - ???


# words and symbols list for calculator_beta

prog_name = 'калькулятор'
ver = 'v1.15'

operators = ['+', '-', '*', '/']
div_opers = ['/', '//', '%']

WRDS = dict(inc='недопустимое значение',
            out='превышен размер числа',
            inp='введите',
            fst='первое',
            num='число',
            opr='оператор',
            prc='вычисляю',
            ans='ответ',
            lad='загрузка',
            tdy='сегодня'
    )

# Load and incorrect
loading = WRDS['lad']
lim_incor = WRDS['out']
unex_incor = f'{WRDS['inc']}: unexpected error/space error'
input_incor = WRDS['inc']
zero_incor = f'{WRDS['inc']}: деление на ноль'

# inputs
ans_txt = WRDS['ans']
inp_txt_1 = f'{WRDS['inp']} {WRDS['fst']} {WRDS['num']} ->'
inp_txt_2 = f'{WRDS['inp']} {WRDS['num']} ->'
inp_oper = f'{WRDS['opr']} ->'
int_txt = 'Целое: '

# Process
sum_txt = f'{WRDS['prc']} сумму'
dif_txt = f'{WRDS['prc']} разность'
prod_txt = f'{WRDS['prc']} произведение'
quot_txt = f'{WRDS['prc']} частное'
