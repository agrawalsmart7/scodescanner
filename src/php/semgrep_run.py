import os
import subprocess
from subprocess import PIPE
from ruamel.yaml import YAML
import shutil
from utils import logs_handler
logger = logs_handler.create_logger(__name__, remote_logging=False)

yaml = YAML()
yaml.preserve_quotes = True
yaml.explicit_start = True


    
def temp_maker(tempdir, listofvariables, homedir):
    rules = homedir+'/rules/php/'
    for filename in os.listdir(rules):
        if filename.startswith('rule') and filename.endswith('yaml'):

            for variable in listofvariables:
                f = open(rules+filename, 'r')
                newf = f.read().replace('$replace', variable.strip())
                overrides = yaml.load(newf)
                with open(tempdir+'rules_'+variable+'_'+filename, 'w') as ff:
                    yaml.dump(overrides, ff)
        elif filename.startswith('all'):
            shutil.copyfile(rules+filename, tempdir+filename)

def sem_initiator(listofvariables, homedir, tempdir):
    for dicts in listofvariables:
        for filename, variables in dicts.items():
            temp_maker(tempdir, variables, homedir)

def sem_runner(homedir, tempdir, outputfile, folder, lines, verbose, jsonfile):
    
    outresults = homedir+'/results/'+outputfile
    logger.info("Running Semgrep on Folder - "+ folder)
    if verbose:
        result = subprocess.run(['semgrep', '--config', tempdir, folder, '--max-lines-per-finding', str(lines),'--verbose'], stdout=PIPE, stderr= PIPE, universal_newlines=True)
    elif jsonfile:
        jsonoutput = homedir+'/results/'+jsonfile
        result = subprocess.run(['semgrep', '--config', tempdir, folder,'--max-lines-per-finding', str(lines), '--json', '-o', jsonoutput], stdout=PIPE, stderr= PIPE, universal_newlines=True)

    else:
        result = subprocess.run(['semgrep', '--config', tempdir, folder, '--max-lines-per-finding', str(lines)], stdout=PIPE, stderr= PIPE, universal_newlines=True)

    if not jsonfile:
        if result.stdout:
            logger.info("Successfully found the Findings - \n")
            logger.info('\n'+result.stdout)
            with open(outresults, 'w') as f:
                f.write(result.stdout)
        elif result.stderr:
            logger.info(result.stderr)

    if jsonfile:
        
        if result.stdout:
            logger.info("Successfully found the Findings - \n")
            logger.info('\n'+result.stdout)
        elif result.stderr:
            logger.info(result.stderr) 