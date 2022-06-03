from ast import Load
from collections import defaultdict
from threading import local
import yaml
from yaml.loader import SafeLoader
import re
from .externalscan import scans
from utils import logs_handler
from .globalvar import h_findings, c_findings, l_findings, m_findings

logger = logs_handler.create_logger(__name__, remote_logging=False) 

def data_retriever(home_dir):
    with open(home_dir+"/rules/yaml/rules.yaml", "r") as e:
        data = yaml.safe_load(e)
        return data


def rules_retriever(home_dir):
    for keys, values in data_retriever(home_dir).items():
        return values


def severity_counter(severity):
    if severity == 'High':
        h_findings.append(True)

    if severity == 'Critical':
        c_findings.append(True)
    
    if severity == 'Medium':
        m_findings.append(True)

    if severity == 'Low':
        l_findings.append(True)

def line_no(filename):
    liness = []
    with open(filename, 'r') as e:
        lines = e.readlines()
        for lineno, line, in enumerate(lines, start=1):
            line = line.split(":")[0]
            line = re.sub(r'[\s+\#]', '', line)
            liness.append({lineno: line})

    return liness

def grep_lineno(filename, value):
    lineno = []
    for lines in line_no(filename):
        for k, v in lines.items():
            if v == value:
                lineno.append(k)
    return lineno 

def zip_results(zip_result):
    line = []
    lineno = []
    for x in zip_result:
        line = x[2]
        lineno = x[1]
    return line, lineno

def sub_runner(filename, match, value, localdicts):
    
    severity_counter(value['severity'])
    lineno = grep_lineno(filename, value['id'])
    zip_result = list(zip(match, lineno))
    for x in zip_result:
        line = x[0]
        lineno = x[1]
        logger.info("Found a Match for Rule: - "+ value['id'] + " - at line no - "+ str(lineno))
        localdicts.setdefault(filename, []).append({"id":value['id'],"line": line ,"lineno":lineno, "message": value['message'], "severity": value['severity']})
    return localdicts


def ext_runner(filename, match, value, localdicts ):
    lineno = grep_lineno(filename, value['id'])
    results = scans(filename, value['id'], value['message'], value['severity'], lineno, match)
    if results:
        for result in results:
            if isinstance(result, list):
                for result in result:
                    values, message, severity, lineno, line = result
                    severity_counter(severity)
                    localdicts.setdefault(filename, []).append({"id":value['id'],"line":[{line: values}] ,"lineno":lineno, "message": message, "severity": severity})

            else:
                values, message, severity, lineno, line = result
                severity_counter(severity)
                localdicts.setdefault(filename, []).append({"id":value['id'],"line":[{line: values}] ,"lineno":lineno, "message": message, "severity": severity})

def runner(filename, home_dir, ignore):
    
    localdicts = defaultdict()
    with open(filename, 'r') as e:
        lines = e.read()
        for value in rules_retriever(home_dir):
            match = re.findall(value['regex'], lines)
            if value['severity'] == ignore:
                pass
            else:
                if match:
                    if 'scan' in value and value['scan'] == True:
                        # logger.info("IMPORTANT: Running External Scan for id - "+ value['id']+"\n")
                        ext_runner(filename, match, value, localdicts  )

                    else:
                        pass
                        
                        sub_runner(filename, match, value, localdicts)
    return localdicts

