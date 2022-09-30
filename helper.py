import shutil
from utils import logs_handler
from src.php.folder_parserer import folderparser, fileparser
from src.yaml.folder_parserer import yaml_fileparser, yaml_folderparser
from src.yaml.output import outresult
import os
from iteration_utilities import unique_everseen
from src.php.semgrep_run import sem_initiator, sem_runner
from src.common.file_sender import jira_issue_creater, slack_issue_creator
from src.php.checking import fp_remover
import tempfile
from src.yaml.globalvar import l_findings, h_findings, m_findings, c_findings

# parser = argparse.ArgumentParser()


# subparser = parser.add_subparsers(dest="command" ,help="Help for more details")

# parser_php = subparser.add_parser("php", help="Check help for PHP language")
# parser_php.add_argument('--default', help='Scan folder inside default Upload folder')
# parser_php.add_argument('--file', help='Please provide file path to Scan file')
# parser_php.add_argument('--folder', help='Scan folder of the specified path')
# parser_php.add_argument('--verbose', help='For verbose running')
# parser_php.add_argument('--maxlines', help='Please provide maxium line numbers', default=3)
# parser_php.add_argument('-o', '--outfile', help='Provide the filename', required=True)
# parser_php.add_argument('--json', help='For Json OutPut')
# parser_php.add_argument('--check', help='Remove False Positives', action='store_true')
# parser_php.add_argument('--jira', help='Send OutPut to your Jira instance', action='store_true')
# parser_php.add_argument('--slack', help='Send OutPut to your Slack WorkSpace Channel', action='store_true')


# parser_yaml = subparser.add_parser("yaml", help="Check help for YAML language")
# parser_yaml.add_argument('--ignore', help='ignore the severity')
# parser_yaml.add_argument('--folder', help='Scan folder of the specified path')
# parser_yaml.add_argument('--file', help='Please provide file path to Scan file')
# parser_yaml.add_argument('-o', '--outfile', help='Provide the filename', required=True)
# parser_yaml.add_argument('--jira', help='Send OutPut to your Jira instance', action='store_true')
# parser_yaml.add_argument('--slack', help='Send OutPut to your Slack WorkSpace Channel', action='store_true')


# argss = parser.parse_args()


# lang = argss.command

# if lang == 'php':
#     default = argss.default
#     folder = argss.folder
#     file = argss.file
#     lines = argss.maxlines
#     verbose = argss.verbose
#     outputfile = argss.outfile
#     jsonfile = argss.json
#     check = argss.check
#     jira = argss.jira
#     slack = argss.slack

# if lang == 'yaml':
    
    # jira = argss.jira
    # slack = argss.slack
    # ignore = argss.ignore
    # folder = argss.folder
    # file = argss.file
    # outputfile = argss.outfile


# print(os.getcwd())
# sys.path.append(os.getcwd+"/src/")

logger = logs_handler.create_logger(__name__, remote_logging=False)


home_dir = os.getcwd()
def php_main(argss, totalfiles):
    default = argss.default
    folder = argss.folder
    file = argss.file
    lines = argss.maxlines
    verbose = argss.verbose
    outputfile = argss.outfile
    jsonfile = argss.json
    check = argss.check
    jira = argss.jira
    slack = argss.slack
    
    os.mkdir(home_dir+"/temp/" )
    tempfile.tempdir = home_dir+"/temp/" # this is to make /temp as temporary directory
    tempdir = tempfile.gettempdir()

    try:
        if folder:
            list_of_variables = list(unique_everseen(folderparser(folder, totalfiles)))
            os.chdir(home_dir)
            sem_initiator(list_of_variables, home_dir, tempdir)
            if jsonfile:
                sem_runner(home_dir, tempdir, outputfile, folder, lines, verbose, jsonfile)
            else:
                sem_runner(home_dir, tempdir, outputfile, folder, lines, verbose, jsonfile=None)
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

def yaml_main(argss, totalfiles):
    jira = argss.jira
    slack = argss.slack
    ignore = argss.ignore
    folder = argss.folder
    file = argss.file
    outputfile = argss.outfile

    if folder:
        if outresult(outputfile, yaml_folderparser(folder, totalfiles, home_dir, ignore), home_dir):
            logger.info("Completed\n")
    elif file:
        if outresult(outputfile, yaml_fileparser(file, home_dir, ignore), home_dir):
            logger.info("Completed")
    else:
        logger.info("\n[!] Please provide the folder to scan\n")

    logger.info("Total Findings found - \nLow: "+str(len(l_findings))+"\nMedium: "+str(len(m_findings))+"\nHigh: "+str(len(h_findings))+"\nCritical: "+str(len(c_findings)))

    if jira and not slack:
        logger.info("Sending File to Jira Instance")
        jira_issue_creater(outputfile)

    if slack and not jira:
        logger.info("Sending File to Slack WorkSpace")
        slack_issue_creator(outputfile)

    
