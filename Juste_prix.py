import random
# 1. Choisir un nombre au hazard
number_to_guess = random.randint(1, 1000)
guess = -1
abandon = False
# 2. Tant que l'utilisateur n'a pas le bon nombre:
while guess != number_to_guess:
    # 2.1 Demander un nombre à l'utilisateur
    instruction = input("Entrez un nombre entre 1 et 1000 [q: quitter]: ")
    #2.2 Vérifier si l'utilisateur veut quitter
    if not instruction.isnumeric():
        if instruction == "q":
            abandon = True
            break
    # 2.3 Vérifier si l'utilisateur a fait une erreur
        else:
            print("Vous avez fait une erreur, réessayer !")
            continue
    # 2.4 Si le nombre est trop petit afficher le message "C'est plus"
    guess = int(instruction)
    if guess < number_to_guess:
        print("C'est plus")
    # 2.5 Si le nombre est trop grand afficher le message "C'est moins"
    elif guess > number_to_guess:
        print("C'est moins")
# 3. Féliciter ou encourager l'utilisateur
if abandon:
    print(f"Dommage, le nombre était {number_to_guess}")
else:
    print(f"Bravo, vous avez trouvé le nombre {number_to_guess}")