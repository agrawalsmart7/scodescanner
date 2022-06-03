from imp import load_source
import yaml
from utils import logs_handler

logger = logs_handler.create_logger(__name__, remote_logging=False) 

def dict_parser(dicts, id):
    for k, v in dicts.items():
        if not isinstance(v, dict):
            if k == id:
                return v
        elif isinstance(v, dict):
            item = dict_parser(v, id)
            if item is not None:
                return item

def parser(content, id):
    list_r = []
    for data in content:
        result = dict_parser(data, id)
        if result:
            list_r.append(result)

    return list_r

# Note: Please Note that
# values = parser(content, id)  These returns values for kubernetes yaml keys for ex:
# rules:
#   - apiGroups: [""]
#     resources: ["*"]
#     verbs: ["*"]
# values will return this - [{apiGroups: [""], resources: ["*"], verbs: ["*"]}]
# so when we are adding any new external function we only need to work with values that makes the process fast and easy. 
# We can see the first line for each function is values = parser(content, id)

def rules(content, id, message, severity, lineno, match):
    
    values = parser(content, id)
    zip_results = list(zip(values, lineno, match))
    high = []
    critical = []
    nothing = []

    any_resources = ['*', 'pods', 'deployments']
    any_verbs = ['*', 'create', 'patch', 'update']

    read_resources = ['secrets', '*']
    read_verbs = ['list', 'get']

    try:
        for lists in zip_results:
            for tuples in lists[0]:
                resourcess = tuples['resources']
                verbs = tuples['verbs']
                
                read_perm = set(read_resources).intersection(set(resourcess))
                read_perm2 = set(read_verbs).intersection(set(verbs))
                
                any_perm = set(any_resources).intersection(set(resourcess))
                any_perm2 = set(any_verbs).intersection(set(verbs))

                if any_perm and any_perm2:
                    message = "IMPORTANT Alert: Dangerous RBAC Permissions defined"
                    logger.info("\nIMPORTANT Alert: Dangerous RBAC Permissions defined")
                    severity = 'Critical'
                    critical.append(tuple((tuples, message, severity, lists[1], lists[2])))

                elif read_perm and read_perm2:
                    message = "IMPORTANT1: Full or Secrets Read Permissions defined"
                    logger.info("\nIMPORTANT1: Full or Secrets Read Permissions defined")
                    severity = 'High'
                    high.append(tuple((tuples, message, severity, lists[1], lists[2])))
    except KeyError:
        pass
    except Exception as e:
        logger.error(e)
    
    if critical and not high:
        return critical

    elif high and not critical:
        return high

    elif high and critical:
        return [high, critical]

    else:
        logger.info("[ALERT] No vulnerable RBAC permisions found")
        message = "No vulnerable RBAC permisions found"
        severity = None
        nothing.append(tuple((values, message, severity, None, None)))
        return nothing


def allowedCapabilities(content, id, message, severity, lineno, match):
    values = parser(content, id)
    zip_results = list(zip(values, lineno, match))
    critical = []

    for lists in zip_results:
        if '*' in lists[0]:
            logger.info("[ALERT] - Accessive Capabilities given to POD")
            message = "Critical Alert: POD contains admin capabilities"
            severity = 'Critical'
            critical.append(tuple((lists[0], message, severity, lists[1], lists[2])))   

        if 'SYS_ADMIN' in values:
            logger.info("[ALERT] - Accessive Capabilities given to POD")
            message = "Critical Alert: POD contains SYS_ADMIN capabilities"
            severity = 'Critical'
            critical.append(tuple((lists[0], message, severity, lists[1], lists[2])))  

    return critical

def volumes(content, id, message, severity, lineno, match):
    values = parser(content, id)
    zip_results = list(zip(values, lineno, match))
    medium = []
    x = None
    for lists in zip_results:
        for tuples in lists[0]:
            for key, value in tuples.items():
                if key == 'hostPath':
                    if '/' in value['path']:
                        x = True
    if x:
        message = "[Alert] - Root hostPath was found used"
        logger.info(message)
        severity = 'Medium'
        medium.append(tuple((tuples, message, severity, lists[1], lists[2])))
    return medium

# Please add function map here if new functions are added

functions_list = {
    'rules': rules, 
    'allowedCapabilities':allowedCapabilities,
    'volumes': volumes
    
} 

def scans(filename, id, message, severity, lineno, match):
    with open(filename, 'r') as e:
        content = yaml.load_all(e, Loader=yaml.FullLoader)
        return functions_list[id](content, id, message, severity, lineno, match)

