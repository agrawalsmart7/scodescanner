import os
from src.parserer import parser 
from src.globalvar import html_return

def runner(f, file_name, out_result, outdirectory):

    with open(file_name, 'r') as filecon:
        fullcontent = [line.strip() for line in filecon.readlines()]
        results = [{str(line.strip()): number} for number, line in enumerate(f, start=1)]
        
        # this for loop is for finding the variable inside dangerous functions
        indi_prevars, indi_vars, var_dict = parser(results, fullcontent, out_result)
        
        indi_prevars_emp = 0
        indi_vars_emp = 0
        var_dict_emp = 0
        if var_dict:
            var_dict_emp = 1
            for variables, lnfunc in var_dict.items():
                
                info ="[+]VULNERABLE at line:"+str(lnfunc[1]) + "<br> &emsp; Found Variable: "+ str(variables)+ "\t Found Inside &emsp; -- \t &emsp;"+ str(lnfunc[0])+"<br><br>"
                out_result.write(info)
        

        # this for loop is for finding the indivisual variables printed/using unfiltered

        out_result.write("<br>")

        if indi_prevars:
            indi_prevars_emp = 1
            for prevar_dict in indi_prevars:
                for prevars, linenumber in prevar_dict.items():
                    info = "[+]VULNERABLE at linenumber: "+str(linenumber)+ "<br> &emsp; Found unfiltered USE of var \t &emsp;"+ prevars +"<br><br>"
                    out_result.write(info)

        if indi_vars:
            indi_vars_emp = 1
            for vars_dict  in indi_vars:
                for vars, linenumbers in vars_dict.items():
                    info = "[+]VULNERABLE at linenumber: "+str(linenumbers) +"<br> &emsp; Found unfiltered USE of var \t &emsp;"+ vars +"<br><br>"
                    out_result.write(info)
        
        if var_dict_emp == 0 and indi_vars_emp  == 0 and indi_prevars_emp == 0:
            pass
        else:
            
            html_return.append('\n\n<br><br>Please find the result output :- <a href="'+outdirectory+'">Output file</a>')
            