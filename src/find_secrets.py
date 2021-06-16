import re
from src.regexes import regex6
from src.check_functions import check_func
from utils import logs_handler

def secret_finder(content):

    results = re.findall(regex6, content)
    
    if results:
        for result in results:
            