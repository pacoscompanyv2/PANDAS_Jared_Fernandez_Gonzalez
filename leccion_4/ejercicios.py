import pandas as pd

reviews = pd.DataFrame({
    "country": ["Italy", "Portugal", "US", "US", "Spain", "Australia", "New Zealand",
                "Canada", "Germany", "US", "Italy", "France"],
    "points": [87, 87, 87, 87, 87, 96, 95, 90, 87, 88, 92, 94],
    "price": [10.0, 15.0, 14.0, 13.0, 15.0, 45.0, 38.0, 22.0, 12.0, 18.0, 30.0, 60.0],
    "taster_name": ["Kerin O'Keefe", "Roger Voss", "Paul Gregutt", "Alexander Peartree",
                    "Michael Schachner", "Joe Czerwinski", "Joe Czerwinski", "Roger Voss",
                    "Anna Lee C. Iijima", "Paul Gregutt", "Kerin O'Keefe", "Roger Voss"],
    "taster_twitter_handle": ["@kerinokeefe", "@vossroger", "@paulgwine", None,
                               "@wineschach", "@JoeCz", "@JoeCz", "@vossroger", None,
                               "@paulgwine", "@kerinokeefe", "@vossroger"],
    "variety": ["White Blend", "Portuguese Red", "Pinot Gris", "Riesling",
                "Tempranillo-Merlot", "Shiraz", "Sauvignon Blanc", "Pinot Noir",
                "Gewurztraminer", "Cabernet Sauvignon", "Sangiovese", "Pinot Noir"],
})

# 1. cuantas reviews escribio cada taster
reviews_written = reviews.groupby("taster_twitter_handle").size()

# 2. mejor puntaje por precio, ordenado por precio ascendente
best_rating_per_price = reviews.groupby("price")["points"].max().sort_index()

# 3. precio minimo y maximo por variedad
price_extremes = reviews.groupby("variety").price.agg(["min", "max"])

# 4. variedades mas caras (ordenadas por min y luego max, descendente)
sorted_varieties = price_extremes.sort_values(by=["min", "max"], ascending=False)

# 5. promedio de puntaje por reviewer
reviewer_mean_ratings = reviews.groupby("taster_name").points.mean()

# 6. combinaciones pais/variedad mas comunes
country_variety_counts = reviews.groupby(["country", "variety"]).size().sort_values(ascending=False)

if __name__ == "__main__":
    print(reviews_written)
    print(best_rating_per_price)
    print(price_extremes)
    print(sorted_varieties)
    print(reviewer_mean_ratings)
    print(reviewer_mean_ratings.describe())
    print(country_variety_counts)
