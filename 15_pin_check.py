code_pin = 7482
attempts = int(0)
pin_check = 0
while not pin_check == code_pin:
    pin_check = int(input("Merci d'entrer votre code PIN: "))
    if pin_check == code_pin:
        print("Code PIN Correct")
        break
    elif pin_check != code_pin:
        attempts += 1
    if attempts == 3:
        print("Trop d'essais, paiement refusé")
        break
    elif attempts < 3:
        print("Incorrect... réessayer")