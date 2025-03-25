import pymysql
from database_config import DB_CONFIG
from database_connect import connect

def create_database():
    connection = pymysql.connect(host=DB_CONFIG["DB_HOST"], user=DB_CONFIG["DB_USER"
    ], password=DB_CONFIG["DB_PASSWORD"])

    cursor = connection.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_CONFIG['DB_NAME']}")
    
    cursor.close()
    connection.close()

def create_tables():
    connection = connect()
    cursor = connection.cursor()

    cursor.execute('''
                CREATE TABLE IF NOT EXISTS Invoices(
                invoice_number VARCHAR(50) PRIMARY KEY,
                issue_date DATE NOT NULL,
                due_date DATE NOT NULL,	
                customer_name VARCHAR(50) NOT NULL,	
                customer_address VARCHAR(50),
                customerphone VARCHAR(20) NOT NULL,
                suppliercompany VARCHAR(50) NOT NULL,
                suppliercompanyadress VARCHAR(50) NOT NULL,
                phonecompany VARCHAR(20) NOT NULL,
                ordernumber VARCHAR(50) NOT NULL,
                po_number VARCHAR(50) NOT NULL,
                subtotal DECIMAL(10, 2) NOT NULL,
                tax	DECIMAL(10, 2) NOT NULL,
                total_due DECIMAL(10, 2) NOT NULL,
                payment_terms VARCHAR(20) NOT NULL
                );
            ''')
    
    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS Invoice_Items(
                    item_id	 INT AUTO_INCREMENT PRIMARY KEY,
                    invoice_number VARCHAR(50) NOT NULL UNIQUE,
                    ordernumber VARCHAR(50) NOT NULL,	
                    item_description VARCHAR(255) NOT NULL,
                    quantity INT NOT NULL,
                    unit_price	DECIMAL(10, 2) NOT NULL,
                    total_price	DECIMAL(10, 2) NOT NULL,
                    FOREIGN KEY (invoice_number) REFERENCES Invoices(invoice_number)
                    );
                   ''')
    
    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS Payments(
                        payment_id INT	AUTO_INCREMENT PRIMARY KEY,
                        invoice_number VARCHAR(50),
                        payment_date DATE NOT NULL,
                        payment_terms VARCHAR(20) NOT NULL,
                        payment_amount DECIMAL(10, 2) NOT NULL,
                        payment_shipping_handling DECIMAL(10, 2) NOT NULL,
                        FOREIGN KEY (invoice_number) REFERENCES Invoices(invoice_number)
                    );
                   ''')
    connection.commit()
    cursor.close()
    connection.close()