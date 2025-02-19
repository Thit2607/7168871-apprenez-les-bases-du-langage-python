fruits={'pomme':'rouge','banane':'jaune','orange':'orange'}
fruits['kiwi']='vert'
print(fruits)
couleur_banane=fruits.get('banane')
print(f"la banane est {couleur_banane} !!")
fruits['pomme']='vert'
print(fruits)
fruits.pop('banane')
print(fruits)
