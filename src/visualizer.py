import pandas as pd
import matplotlib.pyplot as plt


# Gráfica para ver intentos de logins
def graph_logins():

    df = pd.read_csv(
        "data/logs2.txt", header=None, names=["Date", "User", "Event", "Status"]
    )

    status_count = df["Status"].value_counts()
    status_count.plot(kind="barh", color="violet")

    plt.title("Logins Status")
    plt.xlabel("Attempts")
    plt.show()


# Gráfica para ver tipos de eventos
def graph_events():

    df = pd.read_csv(
        "data/logs2.txt", header=None, names=["Date", "User", "Event", "Status"]
    )

    event_count = df["Event"].value_counts()
    ax = event_count.plot(kind="bar", color="blue")

    for i, v in enumerate(event_count):
        ax.text(i, v, str(v), fontweight="bold")

    plt.show()


# Gráfica para ver eventos realizados por usuarios
def user_events():
    df = pd.read_csv(
        "data/logs2.txt", header=None, names=["Date", "User", "Event", "Status"]
    )

    user_count = df["User"].value_counts()

    plt.figure(figsize=(10, 6))

    user_count.plot(kind="barh", color="orange")

    plt.title("Actividad de los usuarios")
    plt.xlabel("# of events")
    plt.ylabel("Users")
    plt.yticks(fontsize=6)
    plt.tight_layout()

    plt.show()


user_events()
