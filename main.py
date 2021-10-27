shopping_list={
    "warzywniak":["marchew", "ogórek", "sałata"],
    "zoologiczny":["jedzenie dla kota", 'jedzenie dla psa'],
    "piekarnia":["chleb", "ciasto"],
    "mięsny":["szynka", "kurczak"]
    }
product_list=[]
for store in shopping_list:
    products=str(shopping_list[store])
    print(f"Idę do {store.upper()} i kupuję tam {products.upper()}")
    product_list+=shopping_list[store]
print(f"W sumię kupiłem {len(product_list)} produktów.")