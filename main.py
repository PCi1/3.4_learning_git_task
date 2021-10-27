shopping_list={
    "warzywniak":["marchew", "ogórek", "sałata"],
    "zoologiczny":["jedzenie dla kota", 'jedzenie dla psa'],
    "piekarnia":["chleb", "ciasto"],
    "mięsny":["szynka", "kurczak"],
    "komputerowy":['pendrive']
    }
product_list=[]
for store in shopping_list:
    products=str(shopping_list[store])
    print(f"Idę do {store.upper()} i kupuję tam {products.upper()}")
    product_list+=shopping_list[store]
print(f"W sumię kupiłem {len(product_list)} produktów.")
print('Dobrze że mam listę z zakpuami, dzięki niej na 100% niczego zapomnę tak jak zapommniałem o zadaniu 3.4')