import os

# Function to check or create the necessary directories
def check_path():
    # -------|  Variable declaration |-------
    path_input   =  './input'
    path_data    =  './data'
    path_error   =  './dataerror'
    path_output  =  './output'
    okay = False
    # -------| END Variable declaration |-------

    if not os.path.exists(path_input):
        os.makedirs(path_input)
        okay = True

    if not os.path.exists(path_data):
        os.makedirs(path_data)

    if not os.path.exists(path_output):
        os.makedirs(path_output)

    if not os.path.exists(path_error):
        os.makedirs(path_error)
        
    return okay, path_input, path_data, path_error, path_output