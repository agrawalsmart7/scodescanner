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
from src.file_sender import jira_issue_creater, slack_issue_creator
from src.checking import fp_remover
import tempfile, shutil

parser = argparse.ArgumentParser()
rootparser = parser.add_mutually_exclusive_group()
rootparser.add_argument('--default', help='Scan folder inside default Upload folder')
rootparser.add_argument('--folder', help='Scan folder of the specified path')
rootparser.add_argument('--file', help='Please provide file path to Scan file')
parser.add_argument('--verbose', help='For verbose running')
parser.add_argument('--maxlines', help='Please provide maxium line numbers', default=3)
parser.add_argument('--outputfile', help='Provide the filename', required=True)
parser.add_argument('--json', help='For Json OutPut')
parser.add_argument('--jira', help='Send OutPut to your Jira instance', action='store_true')
parser.add_argument('--slack', help='Send OutPut to your Slack WorkSpace Channel', action='store_true')
parser.add_argument('--check', help='Remove False Positives', action='store_true')


argss = parser.parse_args()
default = argss.default
folder = argss.folder
file = argss.file
lines = argss.maxlines
verbose = argss.verbose
outputfile = argss.outputfile
jsonfile = argss.json
check = argss.check
jira = argss.jira
slack = argss.slack



# print(os.getcwd())
# sys.path.append(os.getcwd+"/src/")

logger = logs_handler.create_logger(__name__, remote_logging=False)


def main():

    try:
        if check and jsonfile is None:
            parser.error('Required --json <filename.json> argument if --check is used')

        starttime = time.time()

        logger.info("Starting the scanner - " + str(time.strftime('%l:%M%p %z on %b %d, %Y')) +'\n' )
        
        home_dir = os.getcwd()
        os.mkdir(home_dir+"/temp/" )
        tempfile.tempdir = home_dir+"/temp/" # this is to make /temp as temporary directory
        tempdir = tempfile.gettempdir()
        totalfiles = []

        if folder:
            list_of_variables = list(unique_everseen(folderparser(folder, totalfiles)))
            os.chdir(home_dir)
            sem_initiator(list_of_variables, home_dir, tempdir)
            sem_runner(home_dir, tempdir, outputfile, folder, lines, verbose, jsonfile)
            if check:
                logger.info('\nRunning False Positive Remover\n')
                fp_remover(home_dir, outputfile, jsonfile)
            
            if jira and not slack:
                logger.info("Sending File to Jira Instance")
                jira_issue_creater(home_dir+'/results/'+outputfile)

            if slack and not jira:
                logger.info("Sending File to Slack WorkSpace")
                slack_issue_creator(home_dir+'/results/'+outputfile)


        elif file:
            
            sem_initiator(fileparser(file), home_dir, tempdir)
            sem_runner(home_dir, tempdir, outputfile, folder, lines, verbose, jsonfile)
            if check:
               
                logger.info('\nRunning False Positive Remover\n')
                fp_remover(home_dir, outputfile, jsonfile)
               
            if jira and not slack:
                logger.info("Sending File to Jira Instance")
                jira_issue_creater(home_dir+'/results/'+outputfile)

            if slack and not jira:
                logger.info("Sending File to Slack WorkSpace")
                slack_issue_creator(home_dir+'/results/'+outputfile)
        else:
            logger.info("\n[!] Please provide the folder to scan\n")
        

    finally:
        shutil.rmtree(tempdir)
        
    logger.info("Total Files - "+ str(len(totalfiles))+ "\t Time Taken -" +str(time.time() - starttime))

    

if __name__ == '__main__':
    main()
    