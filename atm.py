
balans = float(input("Bank hesabınızdakı mövcut pul miqdarını yazın:"))

while True:
    if balans == 0:
        print("Pulunuz yoxdur")
        a = input("Seciminizi edin (deposit,exit):")
    else:
        a = input("Seçiminizi edin(deposit,withdraw,exit): ")
    if a=="deposit":
        b = int(input("İstədiyiniz məbləği yazın: "))
        if b > 0:
            balans=balans+ b
            print(b,"elave olundu")
    elif a == "withdraw":
        if balans == 0:
            print("deposit edƏ bilmərsiniz. balans 0dır")
        else:
            b = int(input("İstədiyiniz mebleği yazın: "))
            if b > balans:
                print("pul yeterli deyil")
            else:
                balans=balans - b
                print( balans,"qeder pul cixarildi")

    elif a == "exit":
        print("çıxış olunur ")
        break

print(balans,"qaldı")
