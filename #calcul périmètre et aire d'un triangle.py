#calcul périmètre et aire d'un triangle
from math import *
ct1 = input('entrer la longueur d''un cote ')
cote1=int(ct1)
ct2 = input('entrer une seconde longueur ')
cote2=int(ct2)
ct3= input('entrer un dernier cote ')
cote3=int(ct3)

perim = cote1 + cote2 + cote3
d = perim/2
aire = sqrt(d*(d-cote1)*(d-cote2)*(d-cote3))

print ('Le périmètre du triangle est de: ', perim)
print ('L aire du triangle est de: ', aire)
