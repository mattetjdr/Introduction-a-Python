code_pin = 7482
attempts = int(0)
pin_check = 0
while not pin_check == code_pin:
    pin_check = input("Merci d'entrer votre code PIN: ")
    if not pin_check.isnumeric() or not len(str(pin_check)) == 4:
        print("Code PIN invalide")
        continue
    elif int(pin_check) == code_pin:
        print("Code PIN Correct")
        break
    elif int(pin_check) != code_pin:
        attempts += 1
        if attempts == 3:
            print("Trop d'essais, paiement refusé")
            break
        elif attempts == 1:
            print("Incorrect... 2 essais restants")
        else:
            print("Incorrect... 1 essai restant")