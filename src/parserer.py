import re
from src.regexes import regex1,regex1_1, regway, regex3, regex4_1, regex4_2
from utils import logs_handler

logger = logs_handler.create_logger(__name__, remote_logging=False) 

only_variables = []
dict_file_variables = dict()
pre_variables = []

def parse_helper(content, file_name):

    results = re.findall(regex1, content) #[ find '$test = $_REQUEST["aaaaa"]']
    if results:        
        for result in results:
            only_variable = re.sub(regex1_1, '', result)
            only_variables.append(only_variable.strip())
            dict_file_variables.setdefault(file_name, []).append(only_variable)


    result2 = re.findall(regway, content)
    if result2:
        for result in set(result2):
            pre_variables.append(result.strip())
            dict_file_variables.setdefault(file_name, []).append(result.strip())

    result3 = re.findall(regex3, content)
    # print(result3.groups())
    if result3:
        for result in set(result3):
            only_variable = re.sub(regex1_1, '', str(result))
            dict_file_variables.setdefault(file_name, []).append(only_variable)

    result4 = re.findall(regex4_1, content)
    # print(result3.groups())
    if result4:
        for result in set(result4):
            only_variable = re.sub(regex4_2, '', str(result))
            dict_file_variables.setdefault(file_name, []).append(only_variable)            

def parser(results, file_name): 
    for contents in results:
        for content, number in contents.items():
            parse_helper(content, file_name)
    return dict_file_variables
   