attacker = input("What piece is the attacker? ")
attackee = input("What piece is being attacked? ")

def rook_attack(rook1, rook2):
    attacker_column = rook1[0]
    attacker_row = rook1[1]
    attackee_column = rook2[0]
    attackee_row = rook2[1]

    if attacker_column == attackee_column:
        return True
    elif attacker_row == attackee_row:
        return True
    else:
        return False

print(rook_attack(attacker,attackee))