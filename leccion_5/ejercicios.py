import pandas as pd

reviews = pd.DataFrame({
    "country": ["Italy", "Portugal", "US", "US", "Spain", "Australia", "New Zealand"],
    "points": [87, 87, 87, 87, 87, 96, 95],
    "price": [10.0, 15.0, None, 13.0, 15.0, 45.0, None],
    "region_1": ["Etna", None, "Willamette Valley", "Lake Michigan Shore", "Navarra",
                 "Barossa", None],
})

# 1. tipo de dato de la columna points
dtype = reviews.points.dtype

# 2. points convertido a string
point_strings = reviews.points.astype(str)

# 3. cuantas reviews no tienen precio
n_missing_prices = reviews.price.isnull().sum()

# 4. regiones mas comunes, con nulos como "Unknown", orden descendente
reviews_per_region = reviews.region_1.fillna("Unknown").value_counts().sort_values(ascending=False)

if __name__ == "__main__":
    print(dtype)
    print(point_strings)
    print(n_missing_prices)
    print(reviews_per_region)
