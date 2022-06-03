

from re import L


content = {'apiVersion': 'apps/v1', 'kind': 'Deployment', 'metadata': {'name': 'myservicepod7', 'labels': {'app': 'servicepod'}}, 'spec': {'replicas': 1, 'selector': {'matchLabels': {'app': 'servicepod'}}, 'template': {'metadata': {'annotations': {'vault.hashicorp.com/agent-inject': 'true', 'vault.hashicorp.com/role': 'internal-app', 'vault.hashicorp.com/agent-inject-secret-config': 'internal/data/database/config', 'vault.hashicorp.com/agent-inject-template-config': '{{ with secret "internal/data/database/config" -}}\n  export MYSQL_ROOT_PASSWORD_COMING_FROM_VAULT="{{ .Data.data.password }}"\n{{- end }}\n'}, 'labels': {'app': 'servicepod'}}, 'spec': {'serviceAccountName': 'utk2', 'volumes': [{'name': 'hostvolume', 'hostPath': {'path': '/'}}], 'containers': [{'name': 'php', 'image': 'php:7.2-apache', 'command': ['/bin/bash', '-c'], 'args': ['service apache2 start && sleep infinity'], 'workingDir': '/var/www/html', 'ports': [{'name': 'serviceport', 'containerPort': 80}], 'volumeMounts': [{'name': 'hostvolume', 'mountPath': '/var/www/html'}]}]}}}}

def list_dict_parser(content, id):
    for lists in content:
        for k, v in lists.items():
            if isinstance(v, str):
                if k == id:
                    return v

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
    if dict_parser(content, id):
        print(dict_parser(content, id))
        list_r.append(dict_parser(content, id))
    return list_r


parser(content, 'volumes')
# from operator import itemgetter
# import yaml

# with open('src/yaml/apache.yml', 'r') as e:
#     content = yaml.load_all(e, Loader=yaml.FullLoader)
#     for content in content:
#         for k in content:
#             print(k)