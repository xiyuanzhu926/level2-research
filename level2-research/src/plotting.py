import matplotlib.pyplot as plt

# auction price path plot
def plot_price(df, code):

    d = df[df["code"] == code].sort_values("time")

    plt.figure(figsize=(10,4))
    plt.plot(d["time"], d["price"])

    plt.title("Trade-based Price Discovery")
    plt.xticks(rotation=45)
    plt.show()

def plot_volume(df, code):

    d = df[df["code"] == code].sort_values("time")

    plt.figure(figsize=(10,4))
    plt.bar(d["time"], d["volume"])

    plt.title("Volume Intensity")
    plt.xticks(rotation=45)
    plt.show()

def plot_vwap(df, code):

    d = df[df["code"] == code].sort_values("time")

    plt.figure(figsize=(10,4))
    plt.plot(d["time"], d["price"], label="price")
    plt.plot(d["time"], d["vwap"], label="vwap")

    plt.legend()
    plt.title("Price vs VWAP")
    plt.xticks(rotation=45)
    plt.show()