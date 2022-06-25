import pdfkit
pdfkit.from_url("http://192.168.0.51:8892/guide/", 'out.pdf', configuration=pdfkit.configuration(
                wkhtmltopdf="D:/lib/wkhtmltopdf/bin/wkhtmltopdf.exe"))