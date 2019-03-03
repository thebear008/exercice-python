#Importattion dans une liste de nombre paires et impaires
t1=[35, 24, 5, 10, 40, 48, 59, 11, 26, 37, 48]
t2=[]
t3=[]
i=0
while i<len(t1):
	if t1[i]%2==0:
		t2.append(t1[i])
	else:
		t3.append(t1[i])
	i=i+1
print ("Liste de nombre paires: ", t2)
print ("Liste de nombre impaires: ", t3)
