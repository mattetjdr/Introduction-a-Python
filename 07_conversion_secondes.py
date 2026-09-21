print("Donne moi un nombre en seconde")
secondestot=int(input())
secondes=secondestot % 60
minutestot=secondestot // 60
minutes=minutestot % 60
heures=minutestot // 60
print(str(heures)+"hour(s) "+str(minutes)+" minute(s) "+str(secondes)+" second(s)")