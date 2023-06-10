import datetime

# get current data in format dd/mm/yyyy
def get_current_date(): 
    now = datetime.datetime.now() 
    date_str = now.strftime("%d/%m/%Y") 
    return date_str
