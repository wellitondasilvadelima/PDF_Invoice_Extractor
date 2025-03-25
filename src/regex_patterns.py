from dataclasses import dataclass

@dataclass(frozen=True)
class RegexPatterns:
    ISSUE_DATE : str = r"\d{2}\/\d{2}\/\d{4}|\d{1}\/\d{1}\/\d{4}|\d{2}\/\d{1}\/\d{4}|\d{1}\/\d{2}\/\d{4}"
    DUE_DATE : str = r"DUE DATE:\s\d{2}\/\d{2}\/\d{4}|DUE DATE:\s\d{1}\/\d{1}\/\d{4}|DUE DATE:\s\d{2}\/\d{1}\/\d{4}|DUE DATE:\s\d{1}\/\d{2}\/\d{4}"
    NUM_INVOICE : str =  r"\#\d*"
    ORDER_NUMBER : str = r"ORDER NUMBER:\s\d+"
    SUPPLIER_COMPANY : str = r"INVOICE\s.[^0-9]+"
    SUPPLIER_COMPANY_ADRESS : str = r"\d+\s.*?,\s.*\w{2}\s.\d+\n"
    SUPPLIER_COMPANY_PHONE : str = r"Phone:\s\(\d+\)\s\d+-\d+|Phone:\s\(\d+\)\s\d\s\d+-\d+|Phone:\s\(\d+\)\d+-\d+"
    COSTUMER_NAME: str = r"BILL TO:\s.[A-Za-z\s&.]+"
    COSTUMER_ADDRESS : str = r"\d+\s.[A-Za-z&.,\s]+[0-9]+\s\("
    COSTUMER_PHONE: str = r"\d{1}\s\(\d+\)\s\d+\-\d+"
