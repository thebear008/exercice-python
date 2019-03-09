#Calculatrice avec boutons
from tkinter import*

fen =Tk()
fen.title("Calculatrice avec bouttons")
nb1=""

def ajout(nb):
	global nb1
	nb1 = nb1 + nb
	label ["text"] = nb1

#Définition des fonctions des boutons

def num1():
	ajout("1")

def num2():
	ajout("2")

def num3():
	ajout("3")

def num4():
	ajout("4")

def num5():
	ajout("5")

def num6():
	ajout("6")

def num7():
	ajout("7")

def num8():
	ajout("8")

def num9():
	ajout("9")

def num0():
	ajout("0")

def point():
	ajout(".")

#Définition des fonctions de calcul

def delete():
	global nb1
	nb1 = ""
	nb2 = ""
	label["text"] = ""

def add():
	global nb1,operateur,nb2
	nb2 = float(nb1)
	nb1 =""
	operateur = 1
	

def sous():
	global nb1,operateur,nb2
	nb2=float(nb1)
	nb1 = ""
	operateur = 2
	

def multi():
	global nb1,operateur,nb2
	nb2=float(nb1)
	nb1=""
	operateur = 3
	

def div():
	global nb1,operateur,nb2
	nb2=float(nb1)
	nb1=""
	operateur = 4
	


def egal():
	global nb1
	nb1 = float(nb1) #Définition d'un chiffre de type float qui permet d'accepeter les nomnbres à virgule
	if operateur == 1:
		result = round(nb2 + nb1,10) #Round permet d'arrondir à deux chiffres après la virgule
	if operateur == 2:
		result = round(nb2-nb1,10)
	if operateur == 3:
		result = round(nb2*nb1,10)
	if operateur == 4:
		result = round(nb2/nb1,10)
	label["text"] = result
	nb1 = str(result)
	result = 0

#Définition de la fenêtre d'affichage

label=Label(fen, text="0")
label.place(x=10, y=10)

#Définition des boutons qui apparaitront dans la fenêtre avec appel des fonctions de boutons

bouton=Button(fen, text=" 1 ", command=num1).place(x=10, y =50)
bouton=Button(fen, text=" 2 ", command=num2).place(x=30, y=50)
bouton=Button(fen, text=" 3 ", command=num3).place(x=50, y=50)
bouton=Button(fen, text=" 4 ", command=num4).place(x=10, y=70)
bouton=Button(fen, text=" 5 ", command=num5).place(x=30, y=70)
bouton=Button(fen, text=" 6 ", command=num6).place(x=50, y=70)
bouton=Button(fen, text=" 7 ", command=num7).place(x=10, y=90)
bouton=Button(fen, text=" 8 ", command=num8).place(x=30, y=90)
bouton=Button(fen, text=" 9 ", command=num9).place(x=50, y=90)
bouton=Button(fen, text=" 0 ", command=num0).place(x=10, y=110)
bouton=Button(fen, text=" . ", command=point).place(x=30, y=110)

bouton=Button(fen, text=" C ", command=delete).place(x=50, y=110)
bouton=Button(fen, text=" + ", command=add).place(x=90, y=50)
bouton=Button(fen, text=" - ", command=sous).place(x=110, y=50)
bouton=Button(fen, text=" * ", command= multi).place(x=130, y=50)
bouton=Button(fen, text=" / ", command=div).place(x=150, y=50)
bouton=Button(fen, text=" = ", command=egal).place(x=30, y=150)
fen.mainloop()
