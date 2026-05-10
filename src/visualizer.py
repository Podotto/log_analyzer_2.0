import pandas as pd

df = pd.read_csv("data/logs2.txt", names=["Date", "User", "Event", "Status"])
print(df.head(10))
