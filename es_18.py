'''

        giordano andrea
	ES ,18 pag 55 (Assegnati il 03/10/2022).

 far inserire due numeri 
 creare una lista contenente:
 la somma dei quadrati dei numeri 
 il quadrato della somma dei numeri
 la differenza tra i quadrati dei numeri
 il quadrato della differenza tra i numeri

 ed infine stampa la lista ottenuta

'''

n1=int(input("inserire il primo numero: "))
n2=int(input("inserire il secondo numero: "))
a = [n1^2+n2^2, (n1+n2)^2, n1^2-n2^2, (n1-n2)^2]
print(a)