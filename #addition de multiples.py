#exercice cherhant à additioner des multiples de 03 et 05
print ('veuillez saisir une valeur minimale :')
a=eval(input())
print('veuillez saisir une valeur maximale :')
b=eval(input())
s=0
n=a
while n<=b:
	if n % 3 == 0 and b % 5 ==0:
		s = n + s
	n = n+1
print ('la somme recherchée vaut :', s)
