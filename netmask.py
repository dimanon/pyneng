#!/usr/bin/env python3

def printr_ten(l):
    for i in l:
        print('{:>10}'.format(i), end=' ')

network = input("Enter network, for examle '10.1.1.1/24' : ")
net, mask = network.split('/')
net = net.split('.')

print('Network')

printr_ten(net)
print('\n')

for i in net:
    print('{:010b}'.format(int(i)), end=' ')

print('\n', '-' * 50)


print('Mask', '\n', mask)

count_number = ''.rjust(int(mask), '1').ljust(32, '0')
oktet = [count_number[i:i+8] for i in range(0, 32, 8)]

for i in oktet:
    print('{:>10}'.format(int(i, 2)), end=' ')

print('\n')

printr_ten(oktet)

