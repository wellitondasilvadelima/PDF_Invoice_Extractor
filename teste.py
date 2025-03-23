import pyodbc
drivers = pyodbc.drivers()

# Exibir os drivers
for driver in drivers:
    print(driver)