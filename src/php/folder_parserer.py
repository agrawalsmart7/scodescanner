import os
from src.php.main_runner import runner # Try to use lang variable as this - src.lang.main_runner import runner
from utils import logs_handler
logger = logs_handler.create_logger(__name__, remote_logging=False)

def filerunner(filename):
    list_of_dicts = []
    if filename.endswith(".php"):
        with open(filename, 'r', encoding="utf8") as f:
            list_of_dicts.append(runner(filename))
    return list_of_dicts


def fileparser(filename):
    list_of_dicts = []
    if filename.endswith(".php"):
        with open(filename, 'r', encoding="utf8") as f:
            list_of_dicts.append(runner(filename))
    return list_of_dicts

def folderparser(folder, totalfiles):
    list_of_dicts = []
    os.chdir(folder) # we are at /uploads folder 
    cwd1 = os.getcwd()
    allfolders = [x[0] for x in os.walk(cwd1)]
    for filename in os.listdir(cwd1): 
        if filename.endswith(".php"):
            totalfiles.append(totalfiles)
            filerunner(filename)

    if allfolders:
        for dir in allfolders:
            os.chdir(dir)
            for filename in os.listdir(dir):
                if filename.endswith(".php"):
                    totalfiles.append(filename)
                    file_dir = os.getcwd()
                    filelocation = file_dir+'/'+filename
                    cwd1 = os.getcwd()
                    list_of_dicts.append(runner(filelocation))
    return list_of_dicts