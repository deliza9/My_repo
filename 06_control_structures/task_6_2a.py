# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'

Сообщение должно выводиться только один раз.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""



ip_add = input('Введи айпи адресс: ')

ip_add = ip_add.split('.')


'''
# Проверка адреса
if ip_add[0].isdigit():
    print('отлично')
elif ip_add[1].isdigit():
    print('отлично')
elif ip_add[2].isdigit():
    print('отлично')
elif ip_add[3].isdigit():
    print('отлично')
else:
    print('фигово') 
''' 
    
    
count = len(ip_add)

for n in ip_add:
    #print(n)
    count -= 1
    if ip_add[count].isdigit() and 0 <= int(ip_add[count]) <= 255:
        ip_add[count] = int(ip_add[count])
    else:
        print('Неправильный IP-адрес')
        break
    

    
    
if 1 <=ip_add[0] <= 223:
    print('unicast')
elif 224 <=ip_add[0] <= 239:
    print('multicast')
    
elif ip_add[0] and ip_add[1] and ip_add[2] and ip_add[3] == 255:
    print('local broadcast')
    
elif ip_add[0] == 0 and ip_add[1] == 0 and ip_add[2] == 0 and ip_add[3] == 0:
    print('unassigned')
    
else:
    print('unused')        
    

for n in ip_add:
    if n == 255:
        print('true')



