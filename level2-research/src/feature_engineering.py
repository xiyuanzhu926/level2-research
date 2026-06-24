import pandas as pd

# 9: 15-9:30 auction
def filter_auction(df):

    df = df[
        (df["time"].dt.hour == 9) &
        (df["time"].dt.minute >= 15) &
        (df["time"].dt.minute <= 30)
    ]

    return df


# consecutive 20 days stock selection (with info from 9:15 to 9:30 and continue 20 days)
def select_stocks(df):

    top_codes = df["code"].value_counts().head(5).index

    return df[df["code"].isin(top_codes)]

# feature engineering
def add_features(df):

    df = df.sort_values(["code", "time"])

    df["price"] = df["new_price"]
    df["volume"] = df["new_volume"]
    df["amount"] = df["new_amount"]

    # VWAP proxy
    df["vwap"] = df["amount"].cumsum() / df["volume"].cumsum()

    # liquidity intensity
    df["intensity"] = df["volume"]

    return df