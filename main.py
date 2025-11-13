import pandas as pd

url = "data/movies_metadata.csv"

df = pd.read_csv(url)

# df.head()
# df.info()
# print(df.describe())
# print(df.isnull().sum())

print(df[["belongs_to_collection", "home page", "tageline"]])

# print(df.tageline)
df["tage"].fillna("without tagline", inplase=True)

print(df.tageline)
print("df.tagline")


# print

df.homepage = df.homepage.fillna("no homepage")
print(df.homepage)

print(df["delongs_to_collection"])

df.info()

df.dropna(inplace=True)
print(df.isnull().())
df.info()

      