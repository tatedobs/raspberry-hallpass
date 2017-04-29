import gspread
from datetime import datetime, timedelta
from authorize import authenticate_google_docs
from id_manager import get_name
from LED import green_on, red_on, flashy_flash
import time


gc = authenticate_google_docs()
sh = gc.open('test')
worksheet = sh.get_worksheet(0)

if(worksheet.row_count <= 1):
    is_open = True
elif(worksheet.cell(worksheet.row_count, 4).value == ''):
    is_open = False
else:
    is_open = True
student_name = ''

def scanned(user_id):
    user_name = get_name(user_id)
    if(is_open):
        check_out(user_id)
        worksheet.update_cell(worksheet.row_count, 1, user_name)
    else:
        if(worksheet.cell(worksheet.row_count, 1).value == user_name):
            if(enough_time_passed()):
                check_in()
            else:
                print('wait a couple seconds')
        else:
            print('someone is checked out')
            flashy_flash()

def check_out(name):
    global is_open
    if(is_open):
        red_on()
        student_name = name
        time_out = datetime.now()
        current_date = '%s/%s/%s' % (time_out.month, time_out.day, time_out.year)
        time_out_string = '%s:%s:%s' % (time_out.hour, time_out.minute, time_out.second)
        data_list = [student_name, current_date, time_out_string]
        worksheet.append_row(data_list)

        is_open = False;
    else:
        print('YOU SHALL NOT PASS')

def check_in():
    global is_open
    if(not is_open):
        green_on()
        time_in = datetime.now()
        time_in_string = '%s:%s:%s' % (time_in.hour, time_in.minute, time_in.second)
        worksheet.update_cell(worksheet.row_count, 4, time_in_string)
        worksheet.update_cell(worksheet.row_count, 5, get_time_gone())
        is_open = True;
        student_name = ''
        time.sleep(5)
    else:
        print('YOU SHALL NOT RETURN')

def get_time_gone():
    time_in = datetime.strptime(worksheet.cell(worksheet.row_count, 4).value, '%H:%M:%S')
    time_out = datetime.strptime(worksheet.cell(worksheet.row_count, 3).value, '%H:%M:%S')
    total_time_in = (3600 * time_in.hour) + (60 * time_in.minute) + time_in.second
    total_time_out = (3600 * time_out.hour) + (60 * time_out.minute) + time_out.second
    total_time_gone = str(timedelta(seconds = total_time_in - total_time_out))
    return total_time_gone

def enough_time_passed(isIn):
    time_out = datetime.strptime(worksheet.cell(worksheet.row_count, 3).value, '%H:%M:%S')
    time_now = datetime.now()
    total_time_out = (3600 * time_out.hour) + (60 * time_out.minute) + time_out.second
    total_time_now = (3600 * time_now.hour) + (60 * time_now.minute) + time_now.second
    if(total_time_now - total_time_out >= 5):
        return True
    else:
        return False
