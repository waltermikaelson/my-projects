import random
a=random.randint(1,100)
while True:
 b=int(input("1den 100e qeder seçilmiş ededi texmin edin:"))
 if a==b:
  print('correct')
  break
 elif abs(a-b)<10:
  print('high')

 elif abs(a-b)>10:
  print('low')
