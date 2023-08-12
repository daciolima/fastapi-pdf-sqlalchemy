from fastapi import APIRouter
import pdfkit
import tempfile

from starlette.responses import FileResponse


router = APIRouter()

titulo = "Relatório de Produção"

options = {
    'title': titulo,
    'page-size': 'A4',
    'margin-top': '1in',
    'margin-right': '0.35in',
    'margin-bottom': '1in',
    'margin-left': '0.75in',
    'header-html': 'html-report/header.html',
    'footer-html': 'html-report/footer.html',
    'footer-right': '[page] de [topage]',
    'encoding': "UTF-8",
    'custom-header': [
        ('Accept-Encoding', 'gzip')
    ],
    'cookie': [
        ('cookie-empty-value', '""'),
        ('cookie-name1', 'cookie-value1'),
        ('cookie-name2', 'cookie-value2'),
    ],
    'no-outline': None,
}

@router.get("/report")
def read_root():
    pdfkit.from_file("html-report/despesas_medicos.html", "reports/relatorio-por-medico.pdf", options=options, verbose=True)
    return FileResponse(
                "reports/relatorio-por-medico.pdf",
                media_type="application/pdf",
                filename="relatorio-por-medico.pdf", 
                content_disposition_type="inline")



@router.get("/report-temporario")
def read_root():
    pdf = pdfkit.from_url(
        "file:///Users/daciolima/Documents/DESENVOLVIMENTO/FastAPI/geek-fastapi/html-report/despesas_medicos.html", 
        False, options=options, verbose=True)
    with tempfile.NamedTemporaryFile(mode="w+b", suffix=".pdf", delete=False) as TPDF:
        TPDF.write(pdf)
        return FileResponse(
                TPDF.name,
                media_type="application/pdf",
                filename="relatorio-por-medico.pdf",
                content_disposition_type="inline",
                
                )
