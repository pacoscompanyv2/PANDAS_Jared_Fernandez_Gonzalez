import pandas as pd

reviews = pd.DataFrame({
    "country": ["Italy", "Portugal", "US"],
    "region_1": ["Etna", None, "Willamette Valley"],
    "region_2": [None, None, "Willamette Valley"],
})

# 1. renombrar region_1 y region_2 a region y locale
renamed = reviews.rename(columns={"region_1": "region", "region_2": "locale"})

# 2. renombrar el indice a "wines"
reindexed = reviews.rename_axis("wines", axis="rows")

# 3. combinar dos dataframes con la misma estructura
gaming_products = pd.DataFrame({"title": ["Mouse", "Keyboard"], "score": [120, 95]})
gaming_products["subreddit"] = "r/gaming"
movie_products = pd.DataFrame({"title": ["Poster", "Bluray"], "score": [80, 60]})
movie_products["subreddit"] = "r/movies"
combined_products = pd.concat([gaming_products, movie_products])

# 4. combinar dos dataframes usando una columna en comun (join)
powerlifting_meets = pd.DataFrame(
    {"MeetTown": ["Austin", "Chicago"]}, index=pd.Index([1, 2], name="MeetID")
)
powerlifting_competitors = pd.DataFrame(
    {"MeetID": [1, 1, 2], "Name": ["Ana", "Luis", "Marco"]}
)
powerlifting_combined = powerlifting_meets.join(
    powerlifting_competitors.set_index("MeetID")
)

if __name__ == "__main__":
    print(renamed)
    print(reindexed)
    print(combined_products)
    print(powerlifting_combined)
