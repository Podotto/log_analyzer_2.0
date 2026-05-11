from fpdf import FPDF


def create_report(file_path):
    total_events = 0
    login_success = 0
    login_fail = 0
    user_list = []
    fail_count = {}
    user_count = {}

    with open(file_path) as file_object:
        for record in file_object:
            line = record.strip().split(",")

            user = line[1].strip()
            event = line[2].strip()
            status = line[3].strip()

            total_events += 1
            user_list.append(user)

            if user in user_count:
                user_count[user] += 1
            else:
                user_count[user] = 1

            if event == "LOGIN" and status == "SUCCESS":
                login_success += 1

            if event == "LOGIN" and status == "FAIL":
                login_fail += 1

                if user in fail_count:
                    fail_count[user] += 1
                else:
                    fail_count[user] = 1

    unique_total = 0
    for user in set(user_list):
        unique_total += 1

    suspicious_list = []
    for user in fail_count:
        if fail_count[user] > 3:
            suspicious_list.append(user)

    sorted_users = sorted(user_count.items(), key=lambda item: item[1], reverse=True)

    with open("output/reporte.txt", "w") as report:
        report.write("REPORTE DE ANALISIS DE LOGS\n")
        report.write("---------------------------\n")
        report.write(f"Total de eventos: {total_events}\n")
        report.write(f"Logins exitosos: {login_success}\n")
        report.write(f"Logins fallidos: {login_fail}\n")
        report.write(f"Usuarios únicos: {unique_total}\n\n")

        report.write("Usuarios sospechosos:\n")
        if suspicious_list == []:
            report.write("No hay usuarios sospechosos.\n")
        else:
            for user in suspicious_list:
                report.write(f"{user}\n")

        report.write("\nTop 3 usuarios con más actividad:\n")
        total = 0
        for user, count in sorted_users:
            if total < 3:
                report.write(f"{user}: {count}\n")
                total += 1

    print("¡Reporte generado correctamente!")


def convert_pdf():

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font("Arial", size=12)

    with open("output/reporte.txt", "r") as pdf_report:

        for i in pdf_report:
            pdf.cell(200, 10, txt=i.strip(), ln=1, align="L")

    pdf.output("output/reporte.pdf")
    print("¡PDF generado correctamente!")
