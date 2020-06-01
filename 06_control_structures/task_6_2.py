# -*- coding: utf-8 -*-
"""
Задание 6.2

1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. Определить тип IP-адреса.
3. В зависимости от типа адреса, вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip_add = input('Введи айпи адресс: ')

ip_add = ip_add.split('.')

count = len(ip_add)

for n in ip_add:
    #print(n)
    count -= 1
    ip_add[count] = int(ip_add[count])
    
    
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
