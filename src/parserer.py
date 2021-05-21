import os
import re
from src.regexes import regex1,regex1_1, regex2, regex3, regex4, regex5
from src.check_functions import check_func


def parse_helper(lines, linenumber, out_result, only_variables, vars, indi_prevars, indi_vars):
    

    content = str(lines)
    results = re.findall(regex1, content)
    
    if results:
        
        info = "[!] At Line "+str(linenumber)+ "<br> Variables Contained Pre-Defined PHP Variables found inside code,Checking further if these new variables resides inside any dangerous funtions:"+str(len(results))+" :&#9;"+ str(results)+ "<br><br>"
        out_result.write(info)
        # logger.info(info)
        
        for result in results:
            only_variable = re.sub(regex1_1, '', result)
            only_variables.append(only_variable.strip())
            check_result = check_func(only_variable.strip(), content)
            if check_result:
                vars[only_variable] = [check_result, linenumber]

    result2 = re.findall(regex2, content)
    if result2:
        info ="[!] At Line "+str(linenumber)+ "<br> PHP PRE-Defined Variables found "+ str(len(set(result2)))+" :&#9;"+str(set(result2))+"<br><br>"
        out_result.write(info)
        # logger.info(info)
        if result2:
            for result in set(result2):
                check_result = check_func(result.strip(), content)
                if check_result:
                    vars[result] = [check_result, linenumber]

    result4 = re.findall(regex4, str(content))
    
    if result4: 
        for along_prevars in result4:
            indi_prevars.append({along_prevars:linenumber})

    for only_variable in only_variables:
        new_regex = regex5+re.escape(only_variable)
        result5 = re.findall(new_regex, str(content))
        if result5:
            for alone_vars in result5:
                indi_vars.append({alone_vars:linenumber})

def parser(lines, out_result): 
    only_variables = []
    vars = {}
    indi_prevars = []
    indi_vars = []

    list_lines = []
    for contents in lines:
        for content, number in contents.items():
            parse_helper(content, number, out_result, only_variables, vars, indi_prevars, indi_vars)

    return indi_prevars, indi_vars, vars 

            
