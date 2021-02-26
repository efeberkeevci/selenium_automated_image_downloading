import pandas as pd

data = pd.read_excel(r'./Netsis Tüm Stok Kartları Kategorili 20072020.xlsx')
df = pd.DataFrame(data, columns=["Stok Kodu", "Kategori 2"])

# SELECT KALE PRODUCTS
select_kale = df.loc[df["Kategori 2"] == "KALE"]
select_canakkale_seramik = df.loc[df["Kategori 2"] == "ÇANAKKALE SERAMİK"]
select_kalekim = df.loc[df["Kategori 2"] == "KALEKİM"]
select_kalebodur = df.loc[df["Kategori 2"] == "KALEBODUR"]
all_kale_productcode_list = select_kale["Stok Kodu"].tolist() + select_canakkale_seramik["Stok Kodu"].tolist(
) + select_kalekim["Stok Kodu"].tolist() + select_kalebodur["Stok Kodu"].tolist()

# SELECT HANSGROHE PRODUCTS
select_hansgrohe = df.loc[df["Kategori 2"] == "HANSGROHE"]
hansgrohe_productcode_list = select_hansgrohe["Stok Kodu"].tolist()
# SELECT GEBERİT PRODUCTS
