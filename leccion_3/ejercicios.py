import pandas as pd

reviews = pd.DataFrame({
    "country": ["Italy", "Portugal", "US", "US", "Spain", "Australia", "New Zealand",
                "Canada", "Germany", "US", "Italy", "France"],
    "description": [
        "Aromas include tropical fruit, broom, brimstone and dried herb.",
        "This is ripe and fruity, a wine that is smooth.",
        "Tart and snappy, the flavors of lime flesh and rind.",
        "Pineapple rind, lemon pith and orange blossom.",
        "Blackberry and raspberry aromas show a typical fruity profile.",
        "Bold and tropical, with notes of mango.",
        "Crisp and fruity, tropical fruit on the nose.",
        "Silky and smooth, red fruit dominant.",
        "Savory dried thyme notes accent sunnier flavors.",
        "Bright acidity and fruity red berry notes.",
        "Sangiovese with earthy fruity undertones.",
        "Elegant, with a tropical finish.",
    ],
    "points": [87, 87, 87, 87, 87, 96, 95, 90, 87, 88, 92, 94],
    "price": [10.0, 15.0, 14.0, 13.0, 15.0, 45.0, 38.0, 22.0, 12.0, 18.0, 30.0, 60.0],
    "title": [f"Wine {i}" for i in range(12)],
})

# 1. mediana de points
median_points = reviews.points.median()

# 2. paises representados (sin duplicados)
countries = reviews.country.unique()

# 3. cuantas veces aparece cada pais
reviews_per_country = reviews.country.value_counts()

# 4. precio centrado (precio - precio promedio)
centered_price = reviews.price - reviews.price.mean()

# 5. mejor relacion puntos/precio
bargain_idx = (reviews.points / reviews.price).idxmax()
bargain_wine = reviews.loc[bargain_idx, "title"]

# 6. cuantas veces aparece "tropical" vs "fruity" en description
n_trop = reviews.description.map(lambda desc: "tropical" in desc).sum()
n_fruity = reviews.description.map(lambda desc: "fruity" in desc).sum()
descriptor_counts = pd.Series([n_trop, n_fruity], index=["tropical", "fruity"])

# 7. traducir puntos a estrellas
def stars(row):
    if row.country == "Canada":
        return 3
    elif row.points >= 95:
        return 3
    elif row.points >= 85:
        return 2
    else:
        return 1

star_ratings = reviews.apply(stars, axis="columns")

if __name__ == "__main__":
    print(median_points)
    print(countries)
    print(reviews_per_country)
    print(centered_price)
    print(bargain_wine)
    print(descriptor_counts)
    print(star_ratings)
