import os


# Función para seleccionar archivo
def select_file():

    txt_files = []

    for file in os.listdir("data"):
        if file.endswith(".txt"):
            txt_files.append(file)

    print("Archivos disponibles:")

    for index, file in enumerate(txt_files, start=1):
        print(f"{index}, {file}")

    option = int(input("Selecciona un archivo:"))

    selected_file = txt_files[option - 1]

    return f"data/{selected_file}"


# Función para leer archivo
def read_logs(file_path):

    with open(file_path) as file_object:

        for record in file_object:
            print(record)


if __name__ == "__main__":
    selected_file = select_file()
    read_logs(selected_file)
