from utils import logs_handler
from src.folder_parserer import folderparser, fileparser
from src.globalvar import totalfiles 
import argparse
import time

parser = argparse.ArgumentParser()
rootparser = parser.add_mutually_exclusive_group()
rootparser.add_argument('-de', '--default', help='Scan folder inside default Upload folder')
rootparser.add_argument('-fo', '--folder', help='Scan folder of the specified path')
rootparser.add_argument('-fi', '--file', help='Please provide file path to Scan file')
parser.add_argument('-o', '--outputfile', help='Provide the filename', required=True)


argss = parser.parse_args()
default = argss.default
folder = argss.folder
file = argss.file
outputfile = argss.outputfile

# print(os.getcwd())
# sys.path.append(os.getcwd+"/src/")

logger = logs_handler.create_logger(__name__, remote_logging=False)

def main():
    starttime = time.time()
    if folder:
        #add function for parsing files from folder
        folderparser(folder, outputfile, starttime)

    elif default:
        folderparser(default, outputfile, starttime)
    elif file:
        fileparser(file, outputfile, starttime)
    else:
        logger.info("\n[!] Please provide the folder to scan\n")
    
    
    # logger.info(html_return)
    
    

if __name__ == '__main__':
    main()
    