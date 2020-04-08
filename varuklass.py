#klass för P-uppgift varuprisdatabas Rasmus Larsson

class Vara():
	def __init__(self, namn, antal, pris, kod): #Klassen Vara kommer generera alla objekt i programmet med respektive attribut
		self.namn  = namn
		self.antal = int(antal)
		self.pris  = float(pris)
		self.kod   = int(kod)

	def uppdatera(self, antalsalda): #Metod för att ta bor antal sålda från antalet i lager
		self.antal-=antalsalda
		

	def __str__(self): #skriver ut namn antal och pris för en vara
		string = self.namn + " " + str(self.antal) + " " + str(self.pris) + " " + str(self.kod)
		return string


