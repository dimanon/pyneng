#!/usr/bin/env python3
network = input("Enter network, for examle '10.1.1.1/24' : ")
net, mask = network.split('/')
net = net.split('.')
print('Network')
for i in net:
    print('{:>10}'.format(i), end=' ')

print('\n')

for i in net:
    print('{:010b}'.format(int(i)), end=' ')

print('\n', '-' * 50)


print('Mask', '\n', mask)

mask1 = int(mask.strip('/'))
count_number = ''.rjust(mask1, '1').ljust(32, '0')
oktet = [count_number[:8], 
         count_number[8:16], 
         count_number[16:24], 
         count_number[24:]]

for i in oktet:
    print('{:>10}'.format(int(i, 2)), end=' ')

print('\n')

for i in oktet:
    print('{:>10}'.format(i), end=' ')

print('\n')

#print(int(oktet1, 2), end=' ')
#print(int(oktet2, 2), end=' ')
#print(int(oktet3, 2), end=' ')
#print(int(oktet4, 2))


