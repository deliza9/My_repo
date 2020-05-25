# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
# делаем из строки список
ospf_route = ospf_route.split()
# удаление нулевого(0) и третьего(via) элемента из списка
ospf_route.pop(0)
ospf_route.pop(2)
# добавление щыза 
ospf_route.insert(0, 'OSPF')
# замена [110/41] на 110/41
ospf_route[2]= ospf_route[2].strip('[]') 
#print(ospf_route)


part1 = ['Protocol:', 'Prefix:', 'AD/Metric:', 'Next-Hop:', 'Last update:', 'Outbound Interface:']

print('{:<20} {:<15}'.format(part1[0],ospf_route[0]))
print('{:<20} {:<15}'.format(part1[1],ospf_route[1]))
print('{:<20} {:<15}'.format(part1[2],ospf_route[2]))
print('{:<20} {:<15}'.format(part1[3],ospf_route[3]))
print('{:<20} {:<15}'.format(part1[4],ospf_route[4]))
print('{:<20} {:<15}'.format(part1[5],ospf_route[5]))

