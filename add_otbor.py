from modules import *
from colorama import Fore, Style, init

init()
head = 'term;dep\n'
out = head
print(f'{Fore.CYAN} Dep: From To\n')
choise = input(' -> ')

if ' ' in choise:
    start, finish = choise.split(' ')
    start, finish = int(start), int(finish) + 1
else:
    start = int(choise)
    finish = start + 1

for x in range(start, finish):
    dep, term = str(x), str(x*10+1)
    out += term + ';' + dep + '\n'

p_green('\n' + out + '\n')
text_to_file(out, IN_DATA_PATH + 'otbor.csv')

