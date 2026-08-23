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
    "designation": ["Vulka Bianco", "Avidagos", None, "Reserve Late Harvest",
                    "Ars In Vitro", "Reserve", "Block 5", "Estate", "Shine",
                    "Old Vine", "Riserva", "Grand Cru"],
    "points": [87, 87, 87, 87, 87, 96, 95, 90, 87, 88, 92, 94],
    "price": [None, 15.0, 14.0, 13.0, 15.0, 45.0, 38.0, 22.0, 12.0, 18.0, 30.0, 60.0],
    "province": ["Sicily & Sardinia", "Douro", "Oregon", "Michigan", "Northern Spain",
                 "South Australia", "Marlborough", "Ontario", "Rheinhessen",
                 "California", "Tuscany", "Burgundy"],
    "region_1": ["Etna", None, "Willamette Valley", "Lake Michigan Shore", "Navarra",
                 "Barossa", None, "Niagara", None, "Napa Valley", "Chianti", "Cote de Nuits"],
    "region_2": [None] * 12,
    "taster_name": ["Kerin O'Keefe", "Roger Voss", "Paul Gregutt", "Alexander Peartree",
                    "Michael Schachner", "Joe Czerwinski", "Joe Czerwinski", "Roger Voss",
                    "Anna Lee C. Iijima", "Paul Gregutt", "Kerin O'Keefe", "Roger Voss"],
    "taster_twitter_handle": ["@kerinokeefe", "@vossroger", "@paulgwine", None,
                               "@wineschach", "@JoeCz", "@JoeCz", "@vossroger", None,
                               "@paulgwine", "@kerinokeefe", "@vossroger"],
    "title": [f"Wine {i}" for i in range(12)],
    "variety": ["White Blend", "Portuguese Red", "Pinot Gris", "Riesling",
                "Tempranillo-Merlot", "Shiraz", "Sauvignon Blanc", "Pinot Noir",
                "Gewurztraminer", "Cabernet Sauvignon", "Sangiovese", "Pinot Noir"],
    "winery": ["Nicosia", "Quinta dos Avidagos", "Rainstorm", "St. Julian", "Tandem",
               "Penfolds", "Cloudy Bay", "Inniskillin", "Heinz Eifel", "Opus One",
               "Antinori", "Domaine Leroy"],
})

# 1. columna description
desc = reviews.description

# 2. primer valor de description
first_description = reviews.description.iloc[0]

# 3. primer registro completo
first_row = reviews.iloc[0]

# 4. primeros 10 valores de description
first_descriptions = reviews.description.iloc[0:10]

# 5. registros con index 1, 2, 3, 5, 8
sample_reviews = reviews.loc[[1, 2, 3, 5, 8]]

# 6. columnas especificas de filas especificas
df = reviews.loc[[0, 1, 10, 11], ["country", "province", "region_1", "region_2"]]

# 7. country y variety de los primeros 10 registros
df2 = reviews.loc[:9, ["country", "variety"]]

# 8. vinos de Italia
italian_wines = reviews[reviews.country == "Italy"]

# 9. vinos de Australia o Nueva Zelanda con al menos 95 puntos
top_oceania_wines = reviews[
    (reviews.country.isin(["Australia", "New Zealand"])) & (reviews.points >= 95)
]

if __name__ == "__main__":
    print(desc)
    print(first_description)
    print(first_row)
    print(first_descriptions)
    print(sample_reviews)
    print(df)
    print(df2)
    print(italian_wines)
    print(top_oceania_wines)
