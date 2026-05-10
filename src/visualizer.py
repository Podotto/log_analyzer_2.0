import pandas as pd
import matplotlib.pyplot as plt


def graph_logins():
    df = pd.read_csv(
        "data/logs2.txt", header=None, names=["Date", "User", "Event", "Status"]
    )

    status_count = df["Status"].value_counts()
    status_count.plot(kind="barh", color="violet")

    plt.title("Logins Status")
    plt.xlabel("Attempts")
    plt.show()


graph_logins()
