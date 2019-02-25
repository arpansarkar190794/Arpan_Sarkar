def import1():
    import csv
    cols = []
    with open('Test.csv') as cv:
        rcv = csv.reader(cv, delimiter=',')
        for col in rcv:
            cols.append(col[0:2])
        for item in cols:
            print(item)
import1()
