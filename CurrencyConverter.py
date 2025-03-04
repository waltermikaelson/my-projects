percent=a=22
while True:
 amount=int(input("mebleği daxil edin:"))

 if amount>50 :
     discount=(amount/100)*a
     print("ödenilecek mebleğ:",(amount)-discount)
 else:
  print('ödenilecek mebleğ:',amount)
    
