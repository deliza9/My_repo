# -*- coding: utf-8 -*-
'''
Задание 5.2a

Всё, как в задании 5.2, но, если пользователь ввел адрес хоста, а не адрес сети,
надо преобразовать адрес хоста в адрес сети и вывести адрес сети и маску, как в задании 5.2.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.1/30 - хост из сети 10.0.5.0/30

Если пользователь ввел адрес 10.0.1.1/24,
вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

prefix = input('Введи ip-сеть в формате 10.1.1.0/24:')

#делим введённые данные на ip-address и маску сети
prefix =prefix.split('/')

#забираем из списка ip-address и маску сети
ip = prefix[0]
mask =prefix[1]

#дробим ip-address на октеты
ip = ip.split('.')
oct1, oct2, oct3, oct4 = ip

#выводим ipaddress преобразуя его в десятичную и в двоичную систему исчисления
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
del2_mask = 32-mask
full_bin_mask = ('1' * mask + '0' *del_mask)
#print(full_bin_mask)
moct1 = full_bin_mask[0:8]
moct2 = full_bin_mask[8:16]
moct3 = full_bin_mask[16:24]
moct4 = full_bin_mask[24:32]

print('{:<8} {:<8} {:<8} {:<8}'.format(int(moct1, 2), int(moct2, 2), int(moct3, 2), int(moct4, 2)))
print('{:<8} {:<8} {:<8} {:<8}'.format(int(moct1), int(moct2), int(moct3), moct4))

print('')
print('')



print('')
print(del_mask)
del_mask = '0'*del_mask
print(del_mask)

del_mask = int(del_mask,2)
print(del_mask)

ip = '{:08b}{:08b}{:08b}{:08b}'.format(int(oct1), int(oct2), int(oct3), int(oct4))
print(ip)
print(type(ip))
print(ip[0:-(del2_mask)])
mask_ip = (ip[0:-(del2_mask)] + '0'*del2_mask)
print(mask_ip)
ip_octet1 = mask_ip [0:8]
ip_octet2 = mask_ip [8:16]
ip_octet3 = mask_ip [16:24]
ip_octet4 = mask_ip [24:32]

print('{:<8} {:<8} {:<8} {:<8}'.format(int(ip_octet1, 2), int(ip_octet2, 2), int(ip_octet3, 2), int(ip_octet4, 2)))
print('{:<8} {:<8} {:<8} {:<8}'.format(ip_octet1, ip_octet2, ip_octet3, ip_octet4))

'''
ip
j='{:08b}'.format(int(oct))
ip_network = bin(int(oct1))+bin(int(oct2))+bin(int(oct3))+bin(int(oct4))
print(ip_network) 
'''
#   32 - 24 = 8
#     del_mask
#     
#     
#     
#     

