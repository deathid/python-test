import random


def sum(a,b):
    return a+b

print(sum(1,2))

mylist = [1,2,3,4,5]
print(mylist)

i = 0
while i < 5:
   i += 1
   for j in range(3):
       print(j)
       if j == 2:
           break
   for k in range(3):
       if k == 2:
           continue
       print(k)
   if i > 3:
       break
   print(i)

try:
   f = open('non-exist.txt')
   print('File opened!')
   f.close()
except:
   print('File not exists.')
print('Done')