
x=[10,20,30,40,50,60,70,80,90,100]
num=0
p=0
sum=0
print('Enter positions to add no.s')
p= int(input())
p= p+1
while num<p:
    sum=x[num]+sum
    num=num+1
print(sum)    