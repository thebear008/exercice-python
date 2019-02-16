class Human:
        name = input ("Quel est votre nom ? ")
        first_name = input ("Quel est votre prénom ? ")
        age = input ("Quel est votre âge ? ")
                		
class Male(Human):                
        sexe_m = input ("Etes vous un homme ? ")
		
class Female(Human):
	sexe_f = input ("Etes vous une femme ? ")

liste = [name, first_name, age, sexe_m, sexe_f]
print (liste)

exit()
		

	

	
