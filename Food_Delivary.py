import pandas as pd
from sqlalchemy import create_engine

df=pd.read_csv("Zomato Dataset 2.csv")
# print(df.head())
# print(df.info())
# print(df.describe())
# print(df.shape)
# print(df.columns)
# print(df.duplicated().sum())
# print(df.isnull().sum())

# format columns names
df.columns=df.columns.str.lower()
df.columns=df.columns.str.replace(" ","_")
df=df.rename(columns={'Time_taken (min)':'time_taken_min'})
# print(df.columns)

df["delivery_person_age"]=df["delivery_person_age"].fillna(df["delivery_person_age"].median())
df["city"]=df["city"].fillna(df["city"].mode()[0])
df["delivery_person_ratings"]=df.groupby("city")["delivery_person_ratings"].transform(lambda x:x.fillna(x.median()))
# print(df.isnull().sum())
# print(df.info())

df["order_date"]=pd.to_datetime(df["order_date"],format="%d-%m-%Y")
df["time_orderd"]=pd.to_datetime(df["time_orderd"],errors="coerce")
df["time_order_picked"]=pd.to_datetime(df["time_order_picked"],errors="coerce")
# print(df.info())
# print(df.isnull().sum())

df["time_orderd"]=df.groupby("type_of_order")["time_orderd"].transform(lambda x:x.fillna(x.median()))
df["time_order_picked"]=df.groupby("type_of_order")["time_order_picked"].transform(lambda x:x.fillna(x.median()))
df["weather_conditions"]=df["weather_conditions"].fillna(df["weather_conditions"].mode()[0])
df["road_traffic_density"]=df["road_traffic_density"].fillna(df["road_traffic_density"].mode()[0])
df["multiple_deliveries"]=df["multiple_deliveries"].fillna(df["multiple_deliveries"].median())
df["festival"]=df["festival"].fillna(df["festival"].mode()[0])
# print(df.isnull().sum())
# print(df.info())

import numpy as np

def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Earth's radius in km

    lat1 = np.radians(lat1)
    lon1 = np.radians(lon1)
    lat2 = np.radians(lat2)
    lon2 = np.radians(lon2)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1-a))

    return R * c

df["distance_km"] = df.apply(
    lambda x: haversine(
        x["restaurant_latitude"],
        x["restaurant_longitude"],
        x["delivery_location_latitude"],
        x["delivery_location_longitude"]
    ),
    axis=1
)

# print(df[["distance_km"]].head())

# print(df.columns)

username = "root"
password = "NewPassword123"
host = "localhost"
port = "3306"
database = "delay_time"

engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
)

# print("Connected Successfully!")

df.to_sql(
    name="zomato",
    con=engine,
    if_exists="replace",
    index=False
)

# print("Data uploaded successfully!")


