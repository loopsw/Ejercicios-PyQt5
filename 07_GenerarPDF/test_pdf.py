import pdfkit
path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
#pdfkit.from_url("http://jacksondev.pythonanywhere.com/orla/1", "E:\LOOPSW\QT_Jesus\out.pdf", configuration=config)
#pdfkit.from_file(r"E:\LOOPSW\QT_Jesus\test.html","E:\LOOPSW\QT_Jesus\out2.pdf", configuration=config)
pdfkit.from_string("Hola mundo","E:\LOOPSW\QT_Jesus\out2.pdf", configuration=config)