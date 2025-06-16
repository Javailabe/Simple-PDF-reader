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
    