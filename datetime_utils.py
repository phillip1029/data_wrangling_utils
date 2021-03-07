
from datetime import datetime as dt

def month_str2num(month_name): 
    """convert month name to month number"""
        return dt.strptime(month_name[0:3], "%b").month 
    
def month_num2str(month_number): 
    """convert month number to month name"""
    if isinstance(month_number, int):
        month_num_str = str(month_number)
        return dt.strptime(month_num_str, "%m").strftime("%b") 
    else:
        return dt.strptime(month_number, "%m").strftime("%b") 

 

 




