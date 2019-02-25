print ("Enter a value" )
a = int (input())
print ("Enter b value" )
b = int (input())
print ("Enter c value" )
c = int (input())

if (a >= b) and (a >= c):
   largest = a
elif (b >= a) and (b >= c):
   largest = b
else:
   largest = c

print("The largest number between",a,",",b,"and",c,"is",largest)