for i in range (20):
   print ('Num:',i)

for i in 'ORANGE':
    print(i)

Fruit= ['Orange','Apple','Bannana']
for i in Fruit :
    print (i)

Veg= ['Carrot','Bringle','Tomatoe','Potatoe']
for i in Veg:
    print(i)



for i in range (10,20,2):
    print(i+1)

for i in range (11,21,2):
    print(i)

for i in range (1,20,2):
    print('odd:',i)
    print('even:',i+1)

for i in range (-2,3):
    print (i)

Fruits=['Apple','Bannana','Mango','Orange']
if 'Orange' in Fruits:
    print('Orange')

for i in Orange:
    if i in Fruits:
        print('Orange')

names=['ali','mrudula','arpan','diganta']
for i in names:
    if i != 'arpan':
        continue
print(i)