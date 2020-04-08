#P-uppgift Varuinköp av Magnus Thulin 
from varuklass import *

def lasfil(): # Funktionen som läser filen
	varuObjekt =  []
	file =  open("varor.txt", "r+")
	allLines =  file.readlines()
	for line in   allLines:
		info = line.split()
		nyvara=Vara(info[0],info[1], info[2], info[3]) #in och float ska finnas här
		varuObjekt.append(nyvara)
	return varuObjekt


def sparafil(varor): #Funktion som uppdaterar varudatabasinformationen. 
	file =  open("varor.txt", "w")
	for data in varor:
		data2 = data.namn + " " + str(data.antal)+" "+ str(data.pris) + " " +str(data.kod)+" "+"\n"
		file.write(data2)


def varuinput(varuObjektlista): #inputfunktion som behandlar inmatning från användaren.
	kvittolista=[]
	while True:
		try:
			varuinfo=input("Mata in varukod för respektive vara samt antal")
			if 	varuinfo=="":
				print ("Du har inte matat in något")
				continue
			if varuinfo=="#":
				break
			varuinfo=varuinfo.split()
			objekt=hittavara(varuinfo[0], varuObjektlista)
			if len(varuinfo)>2:
				print("Du kan bara mata en eller två parametrar")
				continue
			if samlaantal(kvittolista, varuinfo) == False:
				kvittolista.append(antal[1])
				uppdateralista(kvittolista, varuObjektlista)
			if len(varuinfo)<2:                          #Om användaren inte skriver in något antal räknar den det som 1 i antal.
				varuinfo.append("1")
				uppdateralista(kvittolista, varuObjektlista)
			if objekt==None:                             #Om varukoden inte finns i databasen talar denna if-sats om detta
				print("Produkten finns ej")
				continue
			if objekt.antal<int(varuinfo[1]):            #kollar om antalet varor är mindre än antalet i lager
				print("\nFör få varor, varan kommer inte läggas till\n")
			else:
				continue

				

			print("För att skriva ut kvittot och avsluta programmet tryck #")
		except ValueError:                              #Ifall en bokstav matas in får användaren följande meddelande
			print("Du kan bara mata in siffror")
	return kvittolista


def samlaantal(kvittolista, varuinfo):
	for vara in kvittolista:
		if vara[0]==varuinfo[0]:
			vara[1]=vara[1]+varuinfo[1]
			return True
	return False




def uppdateralista(kvittolista, varuObjektlista):        #doctest, Funktion för att uppdatera varuprisdatabasen med dess antal
	for info in kvittolista:
		varuObjekt=hittavara(info[0], varuObjektlista)
		varuObjekt.uppdatera(int(info[1]))



def printkvitto(varuObjektlista, kvittolista):           #doctest, Funktion för att printa ut slutgiltiga kvittot.
	print("Varunamn         ", end="")
	print("Antal   ", end="")
	print("A-pris     ", end="")
	print("Summa")
	print("--------------------------------------------------")
	kvittototalpris=0
	totalantal=0
	for info in kvittolista:
		kod=info[0]
		vara=hittavara(kod, varuObjektlista)
		namn=vara.namn
		antal=info[1]
		a_pris=vara.pris
		totalpris=kalkylerapris(a_pris, antal)
		print(namn, " "*(10-len(namn)), end="")
		print(" "*(10-len(antal)), antal, end="")
		print(" "*(10-len(str(a_pris))), round(a_pris), end="")
		print(" "*(10-len(str(totalpris))), totalpris)
		kvittototalpris= kvittototalpris+ totalpris
		totalantal = int(antal) + totalantal
	print("--------------------------------------------------")
	print("Total", " "*(16-len(str(totalantal))), end="")
	print(str(totalantal), " "*(19-len(str(kvittototalpris))), end="")
	print(str(kvittototalpris))


def hittavara(kod, varuObjektlista):                   #doctest, Söker efter kod för matching av dess respektive pris samt varunamn
	kod=int(kod)
	for varuObjekt in varuObjektlista:
		if kod == varuObjekt.kod:
			return varuObjekt



def kalkylerapris(pris, antal):                       #doctest, Funktion för att kalkylera pris (antal*pris)
	totalpris=float(pris)*int(antal)
		
	return totalpris



def main():                                          #kallar på den lästa filen som presenteras i menyn och kör alla funktioner
	varuObjekt=lasfil()
	kvittolista=varuinput(varuObjekt)
	printkvitto(varuObjekt, kvittolista)
	uppdateralista(kvittolista, varuObjekt)
	sparafil(varuObjekt)

if __name__ == "__main__":
	main()
