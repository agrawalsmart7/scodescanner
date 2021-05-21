from logging.handlers import HTTPHandler
import re
from utils import logs_handler
import sys
import os
from src.vulnerable_functions import insecure_functions
from src.folder_parserer import folderparser
from src.globalvar import html_return


args = sys.argv[1]
# print(os.getcwd())
# sys.path.append(os.getcwd+"/src/")

logger = logs_handler.create_logger(__name__, remote_logging=False)

def main(folder):
    
    
    #add function for parsing files from folder
    folderparser(folder)
    # logger.info(html_return)
    
    

if __name__ == '__main__':
    main(args)
    