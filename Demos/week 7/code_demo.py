'''f1 =open("john.txt")
f2=open("harry.txt")

for i in range(3):
  print(f"\033[92mJohn:{f1.readline()}\033[0m", end="")
  print(f"\033[93m(Harry: {f2.readline()}\033[0m",end="")

f1.close()
f2.close()'''


'''import csv
with open("fold1/fold2/data.csv") as d :
  reader = csv.reader(d,delimiter=",",quotechar="'")
  for row in reader:
    print(row)'''
'''
f =open("fold1/fold2/data.csv","w")
lista =['name','mark','telephone']

for i in lista:

  f.write(i)
  f.write(',')
  '''