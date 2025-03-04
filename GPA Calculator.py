fenn1=int(input())
fenn2=int(input())
fenn3=int(input())
fenn4=int(input())
fenn5=int(input())

a=fenn_ortalamasi=(fenn1+fenn2+fenn3+fenn4+fenn5)/5
if 90<a<100:
    print('çox yaxşı')

elif 80<a<90:
    print('yaxşı')
elif 70<a<80:
    print('orta')
elif 50<a<70:
    print('pis')
