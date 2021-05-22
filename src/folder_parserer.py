import os
from src.globalvar import html_return
from src.main_runner import runner

def folderparser(folder):
    directory = "uploads/"+folder+'/'
    outdirectory = 'results/out_'
    os.chdir(directory) # we are at /uploads/folder 
    for filename in os.listdir(os.getcwd()):
        # outdirectory = outdirectory
        # print(outdirectory)
        with open('../../results/out_'+filename,'a') as out_result:
            if filename.endswith(".php"):
                with open(filename, 'r', encoding="utf8") as f:
                    runner(f, filename, out_result, outdirectory+filename)

    if html_return:
        for html in set(html_return):
            print(html)