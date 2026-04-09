full_dot = '●'
empty_dot = '○'

def create_character(character_name,strength,intelligence,charisma):
    if not isinstance(character_name,str):
        return "The character name should be a string"

    elif character_name == "" or character_name == " ":
        return "The character should have a name"
    elif len(character_name) > 10:
        return "The character name is too long"
    elif " " in character_name:
        return "The character name should not contain spaces"
    elif not isinstance(strength,int) or not isinstance(intelligence,int) or not isinstance(charisma,int):
        return "All stats should be integers"
    elif strength < 1 or intelligence < 1 or charisma < 1:
        return "All stats should be no less than 1"
    elif strength > 4 or intelligence > 4 or charisma > 4:
        return "All stats should be no more than 4"
    elif not((strength + intelligence + charisma) == 7):
        return "The character should start with 7 points"
    else:
        strength_dots = "\nSTR " + full_dot * strength + empty_dot * (10-strength)
        intelligence_dots = "\nINT " + full_dot * intelligence + empty_dot * (10-intelligence)
        charisma_dots = "\nCHA " + full_dot * charisma + empty_dot * (10-charisma)
        to_return = "Character Name: " + character_name + strength_dots + intelligence_dots + charisma_dots
        return to_return
    
print(create_character("Megan",3,3,1))