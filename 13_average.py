print("""Bienvenue dans ce programme pour calculer ta moyenne.
Tape 'q' à tout moment pour quitter la boucle.""")
note = 0
instruction = 0
number_of_notes = 0
while instruction != "q":
    instruction = input("Insère une note sur 20 : ")
    if not instruction.isnumeric():
        print("Valeur invalide")
        continue
    elif instruction.isnumeric():
        if int(instruction) < 0 and instruction > 20:
            print("Valeur trop basse ou trop haute")
            continue
        else:
            note = note + instruction
            number_of_notes += 1
moyenne = float(note) / float(number_of_notes)
print(f"Ta moyenne est de {moyenne}/20")