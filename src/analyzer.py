# Total de eventos
def total_events(file_path):
    total = 0

    with open(file_path) as file_object:
        for record in file_object:
            total += 1

    print(f"Total de eventos: {total}")


# Successful Logins
def login_success(file_path):
    total = 0

    with open(file_path) as file_object:
        for record in file_object:
            line = record.strip().split(",")

            event = line[2].strip()
            success = line[3].strip()

            if event == "LOGIN" and success == "SUCCESS":
                total += 1

    print(f"Logins exitosos: {total}")


# Failed Logins
def login_fail(file_path):
    total = 0

    with open(file_path) as file_object:
        for record in file_object:
            line = record.strip().split(",")

            event = line[2].strip()
            success = line[3].strip()

            if event == "LOGIN" and success == "FAIL":
                total += 1

    print(f"Logins fallidos: {total}")


# Unique users
def unique_users(file_path):
    total = 0
    user_list = []

    with open(file_path) as file_object:
        for record in file_object:
            line = record.strip().split(",")
            user = line[1].strip()
            user_list.append(user)

    for i in set(user_list):
        total += 1

    print(f"Usuarios únicos: {total}")


# Usuarios sospechosos
def suspicious_users(file_path):
    fail_count = {}

    with open(file_path) as file_object:
        for record in file_object:
            line = record.strip().split(",")
            user = line[1].strip()
            event = line[2].strip()
            status = line[3].strip()

            if event == "LOGIN" and status == "FAIL":
                if user in fail_count:
                    fail_count[user] += 1
                else:
                    fail_count[user] = 1

    print("Usuarios sospechosos:")
    found = False

    for user in fail_count:
        if fail_count[user] > 3:
            print(user)
            found = True

    if found == False:
        print("No hay usuarios sospechosos.")


# Top 3 usuarios con más actividad
def top_users(file_path):
    user_count = {}

    with open(file_path) as file_object:
        for record in file_object:
            line = record.strip().split(",")
            user = line[1].strip()

            if user in user_count:
                user_count[user] += 1
            else:
                user_count[user] = 1

    sorted_users = sorted(user_count.items(), key=lambda item: item[1], reverse=True)

    print("Top 3 usuarios con más actividad:")

    total = 0
    for user, count in sorted_users:
        if total < 3:
            print(f"{user}: {count}")
            total += 1
