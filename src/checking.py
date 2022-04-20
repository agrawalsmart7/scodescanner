from email.policy import default
import time
import json
import os
import re
from utils import logs_handler
logger = logs_handler.create_logger(__name__, remote_logging=False)

split = '\w+\/.*?\.[\w]+\.php'

filepath = '../results/out1.json'

reg = r'(?:GET|POST|REQUEST|COOKIE|FILES|SESSION)\[[\'\"][A-Za-z0-9_-]+[\'\"]\]'
regway = r'(\$_'+reg+')' # indivisual variables such as $_GET['aa'] or $getParam['bbb']
regex1 = r'\$\w+.\=+.'+regway 
checkid = {}
checkid_list_of_indivisual_vars = []


def newoutput(out, txtfileoutput):
    check_id = out['check_id']
    filepath1 = out['path']
    lines = out['extra']['lines']
    line_no = out['start']['line']
    message = out['extra']['message']

    with open('results/'+txtfileoutput, 'a') as f:
        f.write(filepath1+'\n')
        f.write('\t'+check_id+'\n')
        f.write('\t\t'+message+'\n')
        f.write('\t\t'+str(line_no)+ ' -- '+ str(lines)+'\n\n\n')


def variable_grepper(check_id):
    try:

        new_strr, var = check_id.split('=', maxsplit=1)
        var = var.strip()
        if not var.startswith("$_"):
            return var
    except ValueError:
        return None
    

def fp_remover(homedir, txtfileoutput, filepath):
    idtobedeleted = []
    
    with open(homedir+'/results/'+filepath, 'r') as f:
        out = json.load(f)
        for i in range(len(out['results'])):
            check_id = out['results'][i]['check_id']

            variable = variable_grepper(check_id)
            filepath1 = out['results'][i]['path']
            if variable:
                variable = variable.replace('$', '\$')
                with open(homedir+'/'+filepath1, 'r') as readfile: 
                    if not re.search(variable+' = \$\_(?:GET|POST|REQUEST|COOKIE|FILES|SESSION)\[[\'\"][A-Za-z0-9_-]+[\'\"]\]', readfile.read()):
                        logger.info(variable + str(out['results'][i]['end']['line'])+ filepath1)
                        
                        idtobedeleted.append({filepath1:out['results'][i]['end']['line']})

        ranges = range(len(out['results']))
        indexestobedeleted = []
        try:
            for lists in out['results']:
                line_no = out['results'][out['results'].index(lists)]['end']['line']
                for dicts in idtobedeleted:
                    for key, values in dicts.items():
                        if line_no == values:
                            indexestobedeleted.append(out['results'].index(lists))

            for i in sorted(indexestobedeleted, reverse=True):
                out['results'].pop(i)

            for ii in range(len(out['results'])):  
                newoutput(out['results'][ii], txtfileoutput)
        except IndexError as e:
            logger.error("No other elements were found inside Json File")