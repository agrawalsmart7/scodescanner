from asyncio import subprocess
import os, sys
from subprocess import PIPE
import subprocess
import re
from ruamel.yaml import YAML
from pathlib import Path

os.chdir('/Users/uagrawal/pentesting/tools/scodescanner')
oscwd = os.getcwd()
configs_path = oscwd+"/rules/rule1.yaml"
result = subprocess.check_output(['semgrep', '--config', configs_path, '/code/test.php'], stderr=subprocess.STDOUT, universal_newlines=True)
print(result.stderr)

    

    # for variable in listofvariables:
    #     with open(oscwd+"/rules/rule1.txt", "rt") as fin:
    #         with open(oscwd+"/rules/rule1.txt", "wt") as fout:
    #             for line in fin:
    #                 print(line)
    #                 fout.write(line.replace('$replace', variable))
        




