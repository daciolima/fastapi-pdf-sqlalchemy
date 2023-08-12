import pdfkit


pdf = pdfkit.from_file("html-report/despesas_medicos.html", "relatorio-por-medico.pdf")
print(pdf)