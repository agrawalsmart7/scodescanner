import re
from src.vulnerable_functions import insecure_functions
from src.globalvar import custom_functions

def check_func(string, content):
    funcs = []
    pre_variables =re.escape(string)
    loc_regex = r'(?:\w+\([^()]*|\w+\(\w+\(*)'+pre_variables+r'[^()]*\)'
    results = re.findall(loc_regex, str(content))
    if results:
        for result in results:
            only_function = re.sub(r'\([^()]*\)', '()', str(result))
            
            only_function2 = re.sub(r'\([^)]*\)', '()', str(only_function))
            if only_function2 in insecure_functions:
                funcs.append(only_function2)
            if only_function in insecure_functions:
                funcs.append(only_function)
            else: 
                custom_functions.append(only_function)


    if funcs:
        return set(funcs)    