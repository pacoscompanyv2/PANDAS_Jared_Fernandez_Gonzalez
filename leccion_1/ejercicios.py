import pandas as pd

# 1. dataframe fruits
fruits = pd.DataFrame({"Apples": [30], "Bananas": [21]})

# 2. dataframe fruit_sales
fruit_sales = pd.DataFrame(
    {"Apples": [35, 41], "Bananas": [21, 34]},
    index=["2017 Sales", "2018 Sales"],
)

# 3. serie ingredients
ingredients = pd.Series(
    ["4 cups", "1 cup", "2 large", "1 can"],
    index=["Flour", "Milk", "Eggs", "Spam"],
    name="Dinner",
)

# 4. leer un csv de reviews de vino
# no tenemos el csv real de kaggle, asi que generamos uno pequeno y lo guardamos
# para poder leerlo igual que en el ejercicio original
sample_reviews = pd.DataFrame({
    "country": ["US", "Spain"],
    "description": ["This tremendous 100% varietal wine...", "Ripe aromas of fig, blackberry..."],
    "designation": ["Martha's Vineyard", "Carodorum Seleccion Especial Reserva"],
    "points": [96, 96],
    "price": [235.0, 110.0],
    "province": ["California", "Northern Spain"],
    "region_1": ["Napa Valley", "Toro"],
    "region_2": ["Napa", None],
    "variety": ["Cabernet Sauvignon", "Tinta de Toro"],
    "winery": ["Heitz", "Bodega Carmen Rodriguez"],
})
sample_reviews.to_csv("winemag-data_first150k.csv")
reviews = pd.read_csv("winemag-data_first150k.csv", index_col=0)

# 5. guardar un dataframe como csv
animals = pd.DataFrame({"Cows": [12, 20], "Goats": [22, 19]}, index=["Year 1", "Year 2"])
animals.to_csv("cows_and_goats.csv")

if __name__ == "__main__":
    print(fruits)
    print(fruit_sales)
    print(ingredients)
    print(reviews)
    print(animals)
