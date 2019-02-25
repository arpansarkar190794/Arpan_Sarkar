def import1():
    import csv
    with open('Test.csv') as cv:
        rcv = csv.reader(cv, delimiter=',')
        for row in rcv:
            print(row[2])
import1()

