** start of main.py **

full_dot = '●'
empty_dot = '○'

def create_character (name,strength,intelligence,charisma):
    if not isinstance(name, str):
        return 'The character name should be a string'
    if name.strip() == "":
        return 'The character should have a name'
    if len(name)>10:
        return 'The character name is too long'
    if ' ' in name:
        return 'The character name should not contain spaces'

    if not isinstance(strength,int):
        return 'All stats should be integers'
    if strength < 1:
        return 'All stats should be no less than 1'
    if strength > 4:
        return 'All stats should be no more than 4'

    if not isinstance(intelligence,int):
        return 'All stats should be integers'
    if intelligence < 1:
        return 'All stats should be no less than 1'
    if intelligence > 4:
        return 'All stats should be no more than 4'

    
    if not isinstance(charisma,int):
        return 'All stats should be integers'
    if charisma < 1:
        return 'All stats should be no less than 1'
    if charisma > 4:
        return 'All stats should be no more than 4'

    sum_stats = strength + intelligence + charisma 
    if sum_stats != 7:
        return 'The character should start with 7 points'

    strength_stat = 'STR ' +  '●'*strength + '○'*(10-strength)
    intelligence_stat = 'INT ' +  '●'*intelligence + '○'*(10-intelligence)
    charisma_stat = 'CHA '+ '●'*charisma + '○'*(10-charisma)
    
    return f"{name}\n{strength_stat}\n{intelligence_stat}\n{charisma_stat}"

character_name = create_character('ren', 4, 2, 1)
print (character_name)






** end of main.py **
