class Compte_Bancaire(object):
	def __init__ (self, nom = "dupont", solde = 1000):
		self.nom = nom
		self.solde = solde
	def depot (self, depot):
		self.depot = depot
		self.solde = self.solde + self.depot
	def retrait (self, retrait):
		self.retrait = retrait
		self.solde = self.solde - self.retrait
	def affichage (self):
		print ("Bonjour Monsieur ", self.nom, "votre solde est de ", self.solde)
cpte = Compte_Bancaire("Duchemol", 800)
cpte.depot(350)
cpte.retrait(200)
cpte.affichage()
