# -*- coding: utf-8 -*-
'''
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''


prefix = input('Введи ip-сеть в формате 10.1.1.0/24:')

prefix =prefix.split('/')

ip = prefix[0]
mask =prefix[1]

ip = ip.split('.')
oct1, oct2, oct3, oct4 = ip

print('Network:')
print('{:<8} {:<8} {:<8} {:<8}'.format(int(oct1), int(oct2), int(oct3), int(oct4)))
print('{:08b} {:08b} {:08b} {:08b}'.format(int(oct1), int(oct2), int(oct3), int(oct4)))

print('')
print('Mask:')
print('/' + mask)
#print(type(mask))
mask = int(mask)
#print('1' * mask)

del_mask = 32-mask
#print('1' * mask + '0' *del_mask)

full_bin_mask = ('1' * mask + '0' *del_mask)
#print(full_bin_mask)
moct1 = full_bin_mask[0:8]
moct2 = full_bin_mask[8:16]
moct3 = full_bin_mask[16:24]
moct4 = full_bin_mask[24:32]

print('{:<8} {:<8} {:<8} {:<8}'.format(int(moct1, 2), int(moct2, 2), int(moct3, 2), int(moct4, 2)))
print('{:<8} {:<8} {:<8} {:<8}'.format(int(moct1), int(moct2), int(moct3), moct4))

#   32 -24 = 8
#    
#
#
#
#






