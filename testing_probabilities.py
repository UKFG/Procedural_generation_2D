import random
import math

########################## FONCTIONS ##########################

############# FONCTIONS DE CREATION ##############

T_Type_Case = []
T_Type_Case.append(["FTrp",["tempere_tiede","sous-tropical","tropical"],4000,16000])
T_Type_Case.append(["FPlv",["boreal","tempere_frais"],1000,4000])
T_Type_Case.append(["FHmd",["boreal","tempere_frais","tempere_tiede","sous-tropical","tropical"],500,8000])
T_Type_Case.append(["Ftpr",["boreal","tempere_frais","tempere_tiede","sous-tropical","tropical"],250,4000])
T_Type_Case.append(["FSch",["tempere_tiede","sous-tropical","tropical"],1000,2000])
T_Type_Case.append(["Stpe",["tempere_frais"],250,500])
T_Type_Case.append(["MaqS",["boreal"],125,250])
T_Type_Case.append(["FTSc",["tropical"],500,1000])
T_Type_Case.append(["MaqD",["tempere_frais","tempere_tiede","sous-tropical","tropical"],125,250])
T_Type_Case.append(["MaqS",["boreal"],125,250,["sous-humide"]])
T_Type_Case.append(["DsCh",["boreal","tempere_frais","tempere_tiede","sous-tropical","tropical"],0,125])
T_Type_Case.append(["TndS",["sous-polaire"],0,125])
T_Type_Case.append(["Toun",["sous-polaire"],125,1000])
T_Type_Case.append(["Taig",["polaire"],0,500])
T_Type_Case.append(["NULL",[""],0,0])

def Between(val,min,max):
	if val >= min and val <=max :
		return True
	else :
		return False


def Type_Case(T_Type_Case):

	Temperature = random.choice(["polaire","sous-polaire","boreal","tempere_frais","tempere_tiede","sous-tropical","tropical"])
	#print(Temperature)

	if Temperature == "polaire":
		PlAn = random.choice([random.randint(0,125),random.randint(125,250),random.randint(250,500)])

	elif Temperature == "sous-polaire" :
		PlAn = random.choice([random.randint(0,125),random.randint(125,250),random.randint(250,500),random.randint(500,1000)])

	elif Temperature == "boreal" :
		PlAn = random.choice([random.randint(0,125),random.randint(125,250),random.randint(250,500),random.randint(500,1000),random.randint(1000,2000)])

	elif Temperature == "tempere_frais" :
		PlAn = random.choice([random.randint(0,125),random.randint(125,250),random.randint(250,500),random.randint(500,1000),random.randint(1000,2000),random.randint(2000,4000)])

	elif Temperature == "tempere_tiede" or Temperature == "sous-tropical" :
		PlAn = random.choice([random.randint(0,125),random.randint(125,250),random.randint(250,500),random.randint(500,1000),random.randint(1000,2000),random.randint(2000,4000),random.randint(4000,8000)])

	elif Temperature == "tropical" :
		PlAn = random.choice([random.randint(0,125),random.randint(125,250),random.randint(250,500),random.randint(500,1000),random.randint(1000,2000),random.randint(2000,4000),random.randint(4000,8000),random.randint(8000,16000)])

	#print(PlAn)

	i = 0

	while i < len(T_Type_Case) - 1 and not (Temperature in T_Type_Case[i][1] and Between(PlAn,T_Type_Case[i][2],T_Type_Case[i][3])) :
		i += 1
	return T_Type_Case[i][0]

#print(Type_Case(T_Type_Case))


T=[]
for j in range(100000):
	T.append(Type_Case(T_Type_Case))

print("FTrp : ",T.count("FTrp")/1000)
print("Voulu : 8")
print("FPlv : ",T.count("FPlv")/1000)
print("Voulu : 3.5")
print("FHmd : ",T.count("FHmd")/1000)
print("Voulu : 10")
print("Ftpr : ",T.count("Ftpr")/1000)
print("Voulu : ?")
print("FSch : ",T.count("FSch")/1000)
print("Voulu : ?")
print("Stpe : ",T.count("Stpe")/1000)
print("Voulu : 6.9")
print("FTSc : ",T.count("FTSc")/1000)
print("Voulu : 6.9")
print("MaqD : ",T.count("MaqD")/1000)
print("Voulu : ?")
print("MaqS : ",T.count("MaqS")/1000)
print("Voulu : ?")
print("DsCh : ",T.count("DsCh")/1000)
print("Voulu : 19.1")
print("TndS : ",T.count("Tnds")/1000)
print("Voulu : 10.3")
print("Taig : ",T.count("Taig")/1000)
print("Voulu : 10.3")
print("Toun : ",T.count("Toun")/1000)
print("Voulu : 8.0")

"""print("RoEG : ",T.count("RoEG")/1000)
print("Voulu : 7.6")
print("NULL : ",T.count("NULL")/1000)
print("Voulu : 0")"""
