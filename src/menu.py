from src.reader import select_file, read_logs
from src.processor import process_logs
from src.analyzer import (
    total_events,
    login_success,
    login_fail,
    unique_users,
    suspicious_users,
    top_users,
)
from src.report import create_report
from src.visualizer import graph_logins, graph_events, user_events


def mostrar_menu():

    selected_file = ""

    while True:
        print("MENÚ PRINCIPAL")
        print("1. Leer logs")
        print("2. Procesar datos")
        print("3. Analizar datos")
        print("4. Generar reporte")
        print("5. Generar gráficas")
        print("6. Salir")

        option = input("Seleccione una opción: ")

        match option:
            case "1":

                selected_file = select_file()

                if selected_file != "":
                    print("Leyendo logs...")
                    read_logs(selected_file)

            case "2":

                print("Procesando datos...")
                process_logs(selected_file)

            case "3":
                print("Analizando datos...")
                total_events(selected_file), login_success(selected_file), login_fail(
                    selected_file
                ), unique_users(selected_file), suspicious_users(
                    selected_file
                ), top_users(
                    selected_file
                )

            case "4":
                print("Generando reporte...")
                create_report(selected_file)

            case "5":
                print(
                    "1. Gráfica de intentos de logins\n2. Gráfica de eventos\n3. Gráfica de actividad de usuarios"
                )

                option = int(input("¿Cuál gráfica desea visualizar?: "))

                if option == 1:
                    graph_logins(selected_file)

                if option == 2:
                    graph_events(selected_file)

                if option == 3:
                    user_events(selected_file)

                else:
                    print("No es una opción válida.")

            case "6":
                print("Saliendo del programa.")
                break

            case _:
                print("Opción inválida, intenta de nuevo.")


mostrar_menu()
