from genericpath import isdir
import os
from src.globalvar import html_return
from src.main_runner import runner
from utils import logs_handler
logger = logs_handler.create_logger(__name__, remote_logging=False)
import six

def filerunner(filename):

    if filename.endswith(".php"):
        filenames = filename.replace(".php",".html")
        with open('../../results/'+filenames,'a') as out_result:
            with open(filename, 'r', encoding="utf8") as f:
                runner(f, filename, out_result, filenames)

def output_data(results_dir, outputfile):
   
    metadata = """ <body> Found Total number of vulnerable Files: """+ str(len(html_return))
    output = results_dir+outputfile
    with open(output, 'w') as f:
        f.write(metadata)
        for html in set(html_return):
            f.write(html)
        f.write("</body></html>")
    
    os.chdir(results_dir) # chaging directory for the showing outputresults
    if not six.PY2:
        logger.info("\n\nPlease open in the browser:\n  http://localhost:8008/"+outputfile+" \n\n" )
        os.system("python -m http.server 8008")
        
    elif six.PY2:
        logger.info("Please open:  http://localhost:8008/"+outputfile+" in the browser. Thanks for using ScodeScanner" )
        os.system("python -m SimpleHTTPServer 8008")
    else:
        logger.info("Could not able to open the HTTP server, ", exit)

def fileparser(filename, outputfile):
    cwd = os.getcwd()
    results_dir = cwd+'/results/'

    if filename.endswith(".php"):
        ext = os.path.basename(filename)
        filenames = ext.replace(".php",".html")
        with open(results_dir+filenames,'a') as out_result:
            with open(filename, 'r', encoding="utf8") as f:
                runner(f, filename, out_result, filenames)

    if html_return:
       output_data(results_dir, outputfile)
    else:
        logger.info("[-] No vulnerable parameter found :( ")    

def folderparser(folder, outputfile):
    cwd = os.getcwd()
    results_dir = cwd+'/results/'
    # outdirectory = 'results/'
    os.chdir("uploads/"+folder) # we are at /uploads/folder 
    cwd1 = os.getcwd()
    allfolders = [x[0] for x in os.walk(cwd1)]
    for filename in os.listdir(cwd1): 
        filerunner(filename)

    if allfolders:
        for dir in allfolders:
            os.chdir(dir)
            newdir = dir.replace(cwd, "")
            newdir = newdir.replace("\\", '_')
            for filename in os.listdir(dir):
                if filename.endswith(".php"):
                    filenames = filename.replace(".php", ".html")
                    forhtml = newdir+"_"+filenames
                    with open(results_dir+newdir+"_"+filenames,'a') as out_result:
                        with open(filename, 'r', encoding="utf8") as f:
                            runner(f, filename, out_result, forhtml)
                            
    if html_return:
       output_data(results_dir, outputfile)
    else:
        logger.info("[-] No vulnerable parameter found :( ")