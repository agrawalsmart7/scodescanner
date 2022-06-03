import time
from utils import logs_handler
from helper import yaml_main, php_main
import argparse
import shutil
from src.yaml.globalvar import totalfiles

logger = logs_handler.create_logger(__name__, remote_logging=False)
parser = argparse.ArgumentParser()
subparser = parser.add_subparsers(dest="command" ,help="Help for more details")

parser_php = subparser.add_parser("php", help="Check help for PHP language")
parser_php.add_argument('--default', help='Scan folder inside default Upload folder')
parser_php.add_argument('--file', help='Please provide file path to Scan file')
parser_php.add_argument('--folder', help='Scan folder of the specified path')
parser_php.add_argument('--verbose', help='For verbose running')
parser_php.add_argument('--maxlines', help='Please provide maxium line numbers', default=3)
parser_php.add_argument('-o', '--outfile', help='Provide the filename', required=True)
parser_php.add_argument('--json', help='For Json OutPut')
parser_php.add_argument('--check', help='Remove False Positives', action='store_true')
parser_php.add_argument('--jira', help='Send OutPut to your Jira instance', action='store_true')
parser_php.add_argument('--slack', help='Send OutPut to your Slack WorkSpace Channel', action='store_true')

parser_yaml = subparser.add_parser("yaml", help="Check help for YAML language")
parser_yaml.add_argument('--ignore', help='ignore the severity')
parser_yaml.add_argument('--folder', help='Scan folder of the specified path')
parser_yaml.add_argument('--file', help='Please provide file path to Scan file')
parser_yaml.add_argument('-o', '--outfile', help='Provide the filename', required=True)
parser_yaml.add_argument('--jira', help='Send OutPut to your Jira instance', action='store_true')
parser_yaml.add_argument('--slack', help='Send OutPut to your Slack WorkSpace Channel', action='store_true')

argss = parser.parse_args()
lang = argss.command


def main():
    
    starttime = time.time()
    logger.info("Starting the scanner - " + str(time.strftime('%l:%M%p %z on %b %d, %Y')) +'\n' )
    if lang == "php":
        jsonfile = argss.json
        check = argss.check
        if check and jsonfile is None:
            parser.error('Required --json <filename.json> argument if --check is used')    
        php_main(argss, totalfiles)

    if lang == "yaml":  
        yaml_main(argss, totalfiles)
    
    logger.info("Total Files - "+ str(len(totalfiles))+ "\t Time Taken -" +str(time.time() - starttime))

        
if __name__ == '__main__':
    main()