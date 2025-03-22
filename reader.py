import pdfplumber
import re
import item
from datetime import datetime

def pdf_reader(invoice_name,listitems):
    regex_date = r"\d{2}\/\d{2}\/\d{4}|\d{1}\/\d{1}\/\d{4}|\d{2}\/\d{1}\/\d{4}|\d{1}\/\d{2}\/\d{4}"
    regex_duedate = r"DUE DATE:\s\d{2}\/\d{2}\/\d{4}|DUE DATE:\s\d{1}\/\d{1}\/\d{4}|DUE DATE:\s\d{2}\/\d{1}\/\d{4}|DUE DATE:\s\d{1}\/\d{2}\/\d{4}"
    regex_num_invoice = r"\#\d*"
    regex_ordernumber = r"ORDER NUMBER:\s\d+"

    regex_suppliercompany = r"INVOICE\s.[^0-9]+"
    regex_suppliercompanyadress = r"\d+\s.*?,\s.*\w{2}\s.\d+\n"
    regex_phonecompany = r"Phone:\s\(\d+\)\s\d+-\d+|Phone:\s\(\d+\)\s\d\s\d+-\d+|Phone:\s\(\d+\)\d+-\d+"

    regex_costumername= r"BILL TO:\s.[A-Za-z\s&.]+"
    regex_costumeraddress = r"\d+\s.[A-Za-z&.,\s]+[0-9]+\s\("
    regex_costumerphone = r"\d{1}\s\(\d+\)\s\d+\-\d+"

    with pdfplumber.open(f"input/{invoice_name}") as pdf:
        for page in pdf.pages:
            text_extract = page.extract_text()
            tables = page.extract_tables()
    num_invoice = ""
    try:
        num_invoice = re.search(regex_num_invoice, text_extract).group()[1:]
        date = re.search(regex_date, text_extract).group()
        duedate = re.search(regex_duedate, text_extract).group()[10:]
        ordernumber = re.search(regex_ordernumber, text_extract).group()[14:]
        suppliercompanyadress = re.search(regex_suppliercompanyadress, text_extract).group()[:-1]
        suppliercompany = re.search(regex_suppliercompany, text_extract).group()[8:-1].replace("\n", " ")
        phonecompany = re.search(regex_phonecompany, text_extract).group()[7:]
        costumerphone = re.search(regex_costumerphone, text_extract).group()[2:]
        po_number = tables[0][1][1]
        terms = tables[0][1][5]

        # Extrair palavras com suas posições
        words = page.extract_words()
        # Separar palavras manualmente com base na posição X
        bill_to = []
        middle_x = page.width / 2  # Definir um ponto de separação no meio da página

        for word in words:
            x0 = word['x0']  # Posição X inicial do texto
            text = word['text']

            if x0 < middle_x:  # Se estiver na parte esquerda da página, pertence a BILL TO
                bill_to.append(text)

        # Reconstruir os textos separados
        bill_to_text = " ".join(bill_to)

        costumername = re.search(regex_costumername, bill_to_text).group()[9:]
        costumeraddress = re.search(regex_costumeraddress, bill_to_text).group()[:-2]

        listproducts = []
        for i in range(1,len(tables[1])-1):
            if(tables[1][i][0]!="" and tables[1][i][0]!=None):
                items =  (item.product_info(
                                quantity = tables[1][i][0],
                                products = tables[1][i][1],
                                unitprice = tables[1][i][2],
                                total = tables[1][i][3],
                                )
                        )
                listproducts.append(items)

        subtotal = tables[1][11][3]
        salestax = tables[1][12][3]
        shipping_handling = tables[1][13][3]
        duetotal = tables[1][14][3]
        '''
        "-------- Lógica de salvar no banco de dados... -------------"'
        '''
        date_now =  datetime.now().strftime("%d/%m/%Y")
        hour_now =  datetime.now().strftime("%H:%M:%S")
        listitems.append([date_now,hour_now,invoice_name,num_invoice,"COMPLETED","OK"])
        return True
    except Exception as e:
        date_now =  datetime.now().strftime("%d/%m/%Y")
        hour_now =  datetime.now().strftime("%H:%M:%S")
        items = [date_now,hour_now,invoice_name,num_invoice,"Exception","Invoice outside the specified standard: " + str(e)]
        listitems.append(items)
        return False
