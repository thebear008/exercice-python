class Voiture(object):
	def __init__(self, marque = "FORD", couleur = "rouge", pilote = "personne", vitesse = 0):
		self.marque, self.couleur, self.pilote, self.vitesse = marque, couleur, pilote, vitesse	
	def choix_conducteur(self, pilote):
		self.pilote = pilote
	def accelerer(self, taux, duree):
		self.taux, self.duree = taux, duree
		self.vitesse = self.taux * self.duree
	def affiche_tout(self):
		print (self.marque, self.couleur, " pilotée par ", self.pilote, " vitesse = ", self.vitesse, "m/s")


test = Voiture()
test.choix_conducteur('juliette')
test.accelerer(1.3, 20)
test.affiche_tout()
