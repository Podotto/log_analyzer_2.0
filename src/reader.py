def read_logs():
    with open("data/logs.txt") as file_object:

        for record in file_object:
            print(record)


if __name__ == "__main__":
    read_logs()
