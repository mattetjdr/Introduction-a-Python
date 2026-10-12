password = input("Entre ton nouveau mot de passe : ")
password2 = ""
while password2 != password:
    password2 = input("Répète ton mot de passe : ")
    if password2 == password:
        break
    else:
        print("""Ils ne correspondent pas !
Réessaye !""")
print("Ton compte a bien été crée")