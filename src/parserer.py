import re
from src.regexes import regex1,regex1_1, regex2, regex4, regex5, regex6
from src.check_functions import check_func
from utils import logs_handler
from time import sleep

logger = logs_handler.create_logger(__name__, remote_logging=False) 

def parse_helper(content, listresults, linenumber, out_result, only_variables, vars, indi_prevars, indi_vars):

    results = re.findall(regex1, content) #[ find '$test = $_REQUEST["aaaaa"]']

    # vars is a dict 
    # indivars is a list which contains a dict because of line number

    if results:
        
        info = "[!] At Line "+str(linenumber)+ "<br> Variables Contained Pre-Defined PHP Variables found inside code,Checking further if these new variables resides inside any dangerous funtions:"+str(len(results))+" :&#9;"+ str(results)+ "<br><br>"
        out_result.write(info)
        # logger.info(info)
        
        for result in results:
            only_variable = re.sub(regex1_1, '', result)
            only_variables.append(only_variable.strip())
            check_result = check_func(only_variable.strip(), listresults)
            if check_result:
                for check_r in check_result:
                    vars[only_variable] = [check_r[0], check_r[1]]

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
        for along_prevars in result4: # echo $GET["qqq"]
            indi_prevars.append({along_prevars:linenumber})
    
    for only_variable in only_variables:
        new_regex = regex5+re.escape(only_variable)
        result5 = re.findall(new_regex, str(content))
        if result5:
            for alone_vars in result5:
                indi_vars.append({alone_vars:linenumber})
    

def parser(results, fullcontent, out_result): 
    only_variables = []
    vars = {}
    indi_prevars = []
    indi_vars = []
    for contents in results:
        for content, number in contents.items():
            parse_helper(content, results, number, out_result, only_variables, vars, indi_prevars, indi_vars)

    return indi_prevars, indi_vars, vars 

            
