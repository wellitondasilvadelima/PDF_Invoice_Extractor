import pdfplumber
import re
from datetime import datetime
from regex_patterns import RegexPatterns
from decimal import Decimal

def pdf_reader(invoice_name,data_log):

    with pdfplumber.open(f"input/{invoice_name}") as pdf:
        for page in pdf.pages:
            text_extract = page.extract_text()
            tables = page.extract_tables()
    try:
        invoice_number = re.search(RegexPatterns.NUM_INVOICE, text_extract).group()[1:]
        issue_date = re.search(RegexPatterns.ISSUE_DATE, text_extract).group()
        due_date = re.search(RegexPatterns.DUE_DATE, text_extract).group()[10:]
        po_number = tables[0][1][1]
        ordernumber = re.search(RegexPatterns.ORDER_NUMBER, text_extract).group()[14:]
        suppliercompanyadress = re.search(RegexPatterns.SUPPLIER_COMPANY_ADRESS, text_extract).group()[:-1]
        suppliercompany = re.search(RegexPatterns.SUPPLIER_COMPANY, text_extract).group()[8:-1].replace("\n", " ")
        phonecompany = re.search(RegexPatterns.SUPPLIER_COMPANY_PHONE, text_extract).group()[7:]
        customerphone = re.search(RegexPatterns.COSTUMER_PHONE, text_extract).group()[2:]
        terms = tables[0][1][5]

        # Extract words with their positions
        words = page.extract_words()
        # Manually split words based on X position
        bill_to = []
        middle_x = page.width / 2  # Set a separation point in the middle of the page

        for word in words:
            x0 = word['x0']  # Initial X position of text
            text = word['text']

            if x0 < middle_x:  # If it's on the left side of the page, it belongs to BILL TO
                bill_to.append(text)

        # Reconstruct the separated texts
        bill_to_text = " ".join(bill_to)

        customer_name = re.search(RegexPatterns.COSTUMER_NAME, bill_to_text).group()[9:]
        customer_address = re.search(RegexPatterns.COSTUMER_ADDRESS, bill_to_text).group()[:-2]

        listproducts = []
        for i in range(1,len(tables[1])-1):
            if(tables[1][i][0]!="" and tables[1][i][0]!=None):             
                quantity = int(tables[1][i][0])
                description = tables[1][i][1]
                unitprice = Decimal(tables[1][i][2])
                total = Decimal(tables[1][i][3])

                listproducts.append({"quantity":quantity,"description":description,"unitprice":unitprice,"total":total})

        subtotal = Decimal(tables[1][11][3])
        salestax = Decimal(tables[1][12][3])
        shipping_handling = Decimal(tables[1][13][3])
        total_due = Decimal(tables[1][14][3])
        payment_amount= total_due

        # format date
        issue_date = datetime.strptime(issue_date, "%m/%d/%Y").strftime("%Y-%m-%d")
        due_date = datetime.strptime(due_date, "%m/%d/%Y").strftime("%Y-%m-%d")
        payment_date= due_date
        #-----------------------------------------------------------------------
        date_now =  datetime.now().strftime("%d/%m/%Y")
        hour_now =  datetime.now().strftime("%H:%M:%S")
        data_log.append([date_now,hour_now,invoice_name,invoice_number,"COMPLETED","OK"])
        data = {
                "invoice_number" : invoice_number,
                "issue_date" : issue_date,
                "due_date" : due_date,
                "customer_name" : customer_name,
                "customer_address" : customer_address,
                "customerphone":customerphone,
                "suppliercompany":suppliercompany,
                "suppliercompanyadress":suppliercompanyadress,
                "phonecompany":phonecompany,
                "po_number" : po_number,
                "ordernumber":ordernumber,
                "subtotal" : subtotal,
                "salestax" : salestax,
                "total_due" : total_due,
                "payment_shipping_handling":shipping_handling,
                "payment_date" : payment_date, 
                "payment_amount" : payment_amount,
                "payment_terms":terms,
                "products": listproducts}

        return True, data
    
    except Exception as e:
        date_now =  datetime.now().strftime("%d/%m/%Y")
        hour_now =  datetime.now().strftime("%H:%M:%S")
        invoice_number = invoice_number if invoice_number != "" else ""
        items_log = [date_now,hour_now,invoice_name,invoice_number,"Exception","Invoice outside the specified standard: " + str(e)]
        data_log.append(items_log)
        return False, {}
