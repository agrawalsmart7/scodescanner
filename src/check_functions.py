import re
from src.vulnerable_functions import insecure_functions
from src.globalvar import custom_functions

def check_func(string, listresults):
    funcs = []
    pre_variables =re.escape(string)
    loc_regex = r'(?:\w+\([^()]*|\w+\(\w+\(*)'+pre_variables+r'[^()]*\)'
    for contents in listresults:
        if type(contents) != str:
            for content, number in contents.items():
                results = re.findall(loc_regex, content)
                if results:
                    for result in results:
                        only_function = re.sub(r'\([^()]*\)', '()', str(result))
                        
                        only_function2 = re.sub(r'\([^)]*\)', '()', str(only_function))
                        if only_function2 in insecure_functions:
                            funcs.append([only_function2, number])
                        if only_function in insecure_functions:
                            funcs.append([only_function, number])
                        else: 
                            custom_functions.append(only_function)


    if funcs:
        funclist = list(set(tuple(func_list) for func_list in funcs))  
        return funclist   