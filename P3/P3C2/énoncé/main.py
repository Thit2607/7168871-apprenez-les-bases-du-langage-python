from bs4 import BeautifulSoup

# Extraction des informations souhaitées avec Beautiful Soup
with open("index.html", "r") as file:
    soup = BeautifulSoup(file, "html.parser")

# Extraction du titre de la page
title = soup.title.string
print("Titre de la page:", title)

# Extraction du texte de la balise h1
h1_text = soup.find("h1").string
print("Texte de la balise h1:", h1_text)

# Dictionnaire pour stocker les produits
all_products = dict()

# Extraction des noms et des prix des produits dans la liste
products = soup.find_all("li")
for product in products:
    name = product.find("h2").string
    price_str = product.find("p", class_="price").string
    # On sépare la chaine avec " " en liste de mots
    price_list = price_str.split(" ")
    # On récupère le prix (= deuxième mot)
    price_euro = float(price_list[1][:-1])  # Enlever le symbole €
    price_dollar = price_euro * 1.2
    all_products[name] = {"prix": f"{price_euro}€", "prix_dollar": f"${price_dollar:.2f}"}

# Extraction des descriptions des produits dans la liste
for product in products:
    name = product.find("h2").string  # Re-obtenir le nom du produit
    # La description est le dernier élément de la liste des paragraphes
    description = product.find_all("p")[-1].string
    all_products[name]["description"] = description

# Affichage des informations extraites
print("Produits:")
for name, details in all_products.items():
    print(f"Nom: {name}")
    print(f"Prix: {details['prix']}")
    print(f"Prix en dollars: {details['prix_dollar']}")
    print(f"Description: {details['description']}")
    print()
