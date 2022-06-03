from src.php.parserer import parser 
from src.php.globalvar import totalfiles
from utils import logs_handler

logger = logs_handler.create_logger(__name__, remote_logging=False) 


def runner(file_name):

    with open(file_name, 'r', encoding="utf8", errors='ignore') as f:

        totalfiles.append(file_name)
        results = [{str(line.strip()): number} for number, line in enumerate(f, start=1)]
        
        file_variable_dict = parser(results, file_name)

        return file_variable_dict