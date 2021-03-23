from modules import *
from modules_base import *
import os
from colorama import Fore, Style, init

def def_agent():
    h = dict()
    h['shablon1'] = ''
    h['shablon2'] = ''
    h['soft'] = ''
    h['limit'] = ''
    a = file_to_arr(COMON_DATA_PATH)
    for vec in a:
        if ag_cod in vec[0]:
            h['shablon1'] = vec[ColDataShablon1]
            h['shablon2'] = vec[ColDataShablon2]
            h['soft'] = vec[ColDataSoft]
            h['limit'] = vec[ColDataLimit]
            break
    if 'shablon1' in h['shablon1']:
        sos('Незнакомый агент', ag_cod)
    return h



vsyo_zapros = file_to_arr(IN_DATA_PATH + 'vsyo_zapros_vneh_otbor.csv')
head = vsyo_zapros[0]
data = vsyo_zapros[1:]


init()
line = ''
ag_cog = ''

ColDataShablon1 = 5
ColDataShablon2 = 6
ColDataSoft = 7
ColDataLimit = 8

ColTermTerm = 0
ColTermId = 1
ColTermSity = 2
ColTermRegion = 3
ColTermStreet = 4
ColTermHouse = 5
ColTermSerial = 6


fname_out = 'OutTerminals.csv'
out_text = ''

for line in data:
    insert_data = vec_to_hash(head, line)

    terminal = insert_data['termial']
    idd = insert_data['id_terminal']
    if not idd:
        idd = terminal
        
    sity = insert_data['city']
    region = insert_data['region']
    if not region:
        region = sity
    
    street = insert_data['street']
    house = insert_data['hous']
    serial = ''.join(insert_data['serial_number'].split('0')[1:])

    ag_cod = terminal[:3]
    out = ['','','','','','','','','',]

    out[0] = terminal
    out[1] = idd
    out[2] = def_agent()['shablon1']
    out[3] = sity + ', ' + region
    out[4] = street + ', ' + house
    out[5] = def_agent()['shablon2']
    out[6] = def_agent()['soft']
    out[7] = def_agent()['limit']
    out[8] = serial
    
    out_line = ';'.join(out)
    out_text += out_line + "\n"
    print(f'{Fore.BLUE} {out_line}')
full_out_fname = OUT_DATA_PATH + fname_out
text_to_file(out_text, full_out_fname)

