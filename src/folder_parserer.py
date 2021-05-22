import os
from src.globalvar import html_return
from src.main_runner import runner

def folderparser(folder):
    directory = "uploads/"+folder+'/'
    outdirectory = 'results/out_'
    os.chdir(directory) # we are at /uploads/folder 
    listofdir = []
    for filename in os.listdir(os.getcwd()):
        if os.path.isdir(filename):
            listofdir.append(filename)
        if filename.endswith(".php"):
            with open('../../results/out_'+filename,'a') as out_result:
                with open(filename, 'r', encoding="utf8") as f:
                    runner(f, filename, out_result, outdirectory+filename, filename)
    if listofdir:
        for dir in listofdir:
            os.chdir(dir)
            for filename in os.listdir(os.getcwd()):
                if filename.endswith(".php"):
                    forhtml = dir+"_"+filename
                    outdir = outdirectory+forhtml
                    with open('../../../results/out_'+dir+"_"+filename,'a') as out_result:
                        with open(filename, 'r', encoding="utf8") as f:
                            runner(f, filename, out_result, outdir, forhtml)
            os.chdir("../")

    if html_return:
        for html in set(html_return):
            print(html)