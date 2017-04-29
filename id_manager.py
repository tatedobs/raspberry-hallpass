import gspread
from authorize import authenticate_google_docs

gc = authenticate_google_docs()
sh = gc.open('id_list')
worksheet = sh.get_worksheet(0)

def add_user(name, input_id):
    data_list = [input_id, name]
    worksheet.append_row(data_list)

def get_name(input_id):
    cell_location = worksheet.find(input_id)
    user_name = worksheet.cell(cell_location.row, 2)
    return user_name.value

def get_id(name):
    cell_location = worksheet.find(name)
    user_id = worksheet.cell(cell_location.row, 1)
    return user_id.value
