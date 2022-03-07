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

def sem_initiator(listofvariables, homedir, tempdir):
    
    for dicts in listofvariables:
        for filename, variables in dicts.items():
            temp_maker(tempdir, variables, homedir)
    
def temp_maker(tempdir, listofvariables, homedir):
    rules = homedir+'/rules/'
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
            
def sem_runner(homedir, tempdir, outputfile, folder):
    outresults = homedir+'/results/'+outputfile
    result = subprocess.run(['semgrep', '--config', tempdir, folder], stdout=PIPE, stderr= PIPE, universal_newlines=True)
    if result.stdout:
        logger.info('\n'+result.stdout)
        with open(outresults, 'w') as f:
            f.write(result.stdout)
    elif result.stderr:
        logger.error(result.stderr) 