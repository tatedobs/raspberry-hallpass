import gspread
from authorize import authenticate_google_docs

gc = authenticate_google_docs()
def new_worksheet():
    try:
        name = raw_input("To which spreadsheet would you like to add a worksheet?")
        sh = gc.open(name)
    except:
        print('There is no spreadsheet with that name')
        print('')
        new_worksheet()

    worksheet = sh.add_worksheet(title="main", rows="1", cols="5")
    worksheet.update_acell('A1', 'Name')
    worksheet.update_acell('B1', 'Date')
    worksheet.update_acell('C1', 'Time Out')
    worksheet.update_acell('D1', 'Time In')
    worksheet.update_acell('E1', 'Time Gone')

new_worksheet()
