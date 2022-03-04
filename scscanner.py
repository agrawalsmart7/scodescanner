from pdb import find_function
from tracemalloc import start
from typing import final
from utils import logs_handler
from src.folder_parserer import folderparser, fileparser
import argparse
import time
import os
from iteration_utilities import unique_everseen
from src.semgrep_run import sem_initiator, sem_runner
import tempfile, shutil

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
    
    logger.info("Starting the scanner - " + str(time.strftime('%l:%M%p %z on %b %d, %Y')) +'\n' )
    
    home_dir = os.getcwd()
    os.mkdir(home_dir+"/temp/" )
    tempfile.tempdir = home_dir+"/temp/" # this is to make /temp as temporary directory
    tempdir = tempfile.gettempdir()
    totalfiles = []
    try:
        if folder:
            list_of_variables = list(unique_everseen(folderparser(folder, totalfiles)))
            os.chdir(home_dir)
            sem_initiator(list_of_variables, home_dir, tempdir)
            sem_runner(home_dir, tempdir, outputfile, folder)
        elif file:
            
            sem_initiator(fileparser(file), home_dir, tempdir)
            sem_runner(home_dir, tempdir, outputfile, folder)
        else:
            logger.info("\n[!] Please provide the folder to scan\n")
    finally:
        shutil.rmtree(tempdir)
    logger.info("Total Files - "+ str(len(totalfiles))+ "\t Time Taken -" +str(time.time() - starttime))

    

if __name__ == '__main__':
    main()
    