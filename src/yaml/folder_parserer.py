import os
from src.yaml.main_runner import runner
from utils import logs_handler
logger = logs_handler.create_logger(__name__, remote_logging=False)


def yaml_fileparser(filename, home_dir, ignore):
    list_of_dicts = []
    if filename.endswith(".yaml") or filename.endswith(".yml"):
           list_of_dicts.append(runner(filename, home_dir, ignore))

    return list_of_dicts

def yaml_folderparser(folder, totalfiles, home_dir, ignore):
    list_of_dicts = []
    os.chdir(folder) # we are at /uploads folder 
    cwd1 = os.getcwd()
    allfolders = [x[0] for x in os.walk(cwd1)]
    if allfolders:
        for dir in allfolders:
            os.chdir(dir)
            for filename in os.listdir(dir):
                if filename.endswith(".yaml") or filename.endswith(".yml"):
                    totalfiles.append(filename)
                    file_dir = os.getcwd()
                    filelocation = file_dir+'/'+filename
                    list_of_dicts.append(runner(filelocation, home_dir, ignore))
    return list_of_dicts


