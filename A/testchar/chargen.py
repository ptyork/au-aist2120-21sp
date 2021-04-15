import json

# LOAD DATA

with open('character.json') as fi:
    char = json.load(fi)

print(f"OH, Hi there {char['name']}")


# MODIFY DATA

char['name'] = 'REAL Jerkface'
char['str'] = 16
char['booger'] = "green"
char['inv'] = []

# MODIFY INVENTORY

char['inv'].append('Sword of Destruction')
char['inv'].append('Mace of Wonder')

# SAVE DATA 

with open('character.json','w') as fi:
    json.dump(char, fi)
