import re
import inspect
import my_reg_exs as mre

def get_definition_name():
    function_name = inspect.currentframe().f_code.co_name
    return function_name

def get_part_number(text):
    substring = text[1500:2000]
    try:
        match = re.search(mre.part_number, substring)
        if match:
            part_number = match.group()
            return part_number
        else:
            return f"Part number not found"
    except Exception as e:
        return f"""
               Exception in function {get_definition_name}();
               Substring[{substring}];
               Regex[{mre.part_number}];
               Exception[{e}])
               """

def get_date_of_order(text):
    substring = text[0:320]
    try:
        match = re.search(mre.date_of_order, substring)
        if match:
            date_of_order = match.group()
            return date_of_order
        else:
            return f"Date of order not found"
    except Exception as e:
        return f"""
               Exception in function {get_definition_name}();
               Substring [{substring}];
               Regex[{mre.date_of_order}];
               Exception[{e}])
               """
    
def get_price(text):
    substring = text[1500:2000]
    used_regex = None
    try:
        match_a = re.findall(mre.price_a, substring)
        if not match_a:
            match = re.findall(mre.price_b, substring)
            used_regex = mre.price_b
            price = match[0]
            return price
        elif match_a:
            used_regex = mre.price_a
            price = match_a[0]
            return price
        else:
            return f"Price not found"
    except Exception as e:
        return f"""
               Exception in function {get_definition_name}();
               Substring [{substring}];
               Regex[{used_regex}];
               Exception[{e}])
               """

def get_effective_date(text):
    substring = text[1500:2000]
    used_regex = None
    try:
        match_a = re.search(mre.effective_date_a, substring)
        if not match_a:
            match = re.findall(mre.effective_date_b, substring)
            used_regex = mre.effective_date_b
            effective_date = match[0]
            return effective_date
        elif match_a:
            used_regex = mre.effective_date_a
            match = match_a.group()
            effective_date = match[-10:]
            return effective_date
        else:
            return f"Effective date not found"
    except Exception as e:
        return f"""
               Exception in function {get_definition_name}();
               Substring [{substring}];
               Regex[{used_regex}];
               Exception[{e}])
               """
    
def get_ship_from_code(text):
    substring = text[1500:2000]
    try:
        match = re.findall(mre.ship_from_code, substring)
        if match:
            ship_from_code = match[-1]
            return ship_from_code
        else:
            return f"Ship from code not found"
    except Exception as e:
        return f"""
               Exception in function {get_definition_name}();
               Substring [{substring}];
               Regex[{mre.ship_from_code}];
               Exception[{e}])
               """
def get_plant(text):
    substring = text[1500:2000]
    try: 
        match = re.findall(mre.plant, substring)
        if match:
            plant = match[-1]
            return plant
        else:
            return f"Plant not found"
    except Exception as e:
        return f"""
               Exception in function {get_definition_name}();
               Substring [{substring}];
               Regex[{mre.plant}];
               Exception[{e}])
               """