# -*- coding: utf-8 -*-
'''
Задание 4.5

Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2.

Результатом должен быть список: ['1', '3', '8']

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
command2 = 'switchport trunk allowed vlan 1,3,8,9'

command1 = command1.split()
command1= command1[-1]
command1 = command1.split(',')
print(command1)

command2 = command2.split()
command2= command2[-1]
command2 = command2.split(',')
print(command2)

result = list(set(command1) & set(command2))
result = sorted(result)
print(result)
