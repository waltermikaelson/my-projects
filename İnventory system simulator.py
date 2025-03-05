a ={}
for _ in range(3):
    məhsul = input("Məhsulun adını daxil edin: ")
    sayı = int(input("sayını daxil edin: "))
    a[məhsul]=sayı

məhsul = input("Satmaq istədiyiniz məhsulun adını daxil edin: ")
if məhsul in a:
    sayı = int(input(f"Neçə ədəd {məhsul} satmaq istəyirsiniz? "))
    if sayı <= a[məhsul]:
        a[məhsul]= a[məhsul]-sayı
        print(məhsul, "üçün yeni stok miqdarı:", a[məhsul])
    else:
        print("Xəta: Stokda kifayət qədər məhsul yoxdur!")
else:
    print("Xəta: Bu məhsul  yoxdur.")

