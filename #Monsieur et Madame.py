#Monsieur et Madame
i = 1

print ('Pour suivre le programme taper 1 sinon taper 2 ')

i = eval(input())

while i == 1:

	print ('Veuillez saisir votre nom ')

	nom = input()

	print ('Si vous êtes un homme tapez 1 sinon tapez 2 ')

	sexe = eval(input())

	if sexe == 1:
		print ('Cher Monsieur, ', nom)
	else:
		print ('Chère Madame, ', nom)

	print ('Pour suivre le prgoramme taper 1 sinon taper 2 ')

	i = eval(input())
	if i == 2:
		exit()