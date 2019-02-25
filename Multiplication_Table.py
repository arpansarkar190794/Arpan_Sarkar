class multi():
    def insert(self,num):
        for i in range(1, 11):
            print(num, "X", i, "=", num * i)
d=multi()
d.insert(num=int(input('Enter the number')))
