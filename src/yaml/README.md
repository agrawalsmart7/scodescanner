# SCodeScanner

We can run SCodeScanner for scanning yaml files that are use in kubernetes. This is mainly focuses on scanning kubernetes configuration files. The scanner will find the vulnerable flags and report all the findings in JSON format with severity and line and line numbers mentioned. We can create our own rules very easily. To create any rules please follow the below.


## How to run?

We need to pass the folder which contains yaml/yml files or file.

`python3 scodescanner.py yaml --folder <foldername> -o <filename>.json`

## How does it work?

1) The tool will retrieve all the rules from the rules.yaml file stored in rules/yaml folder.

2) It searches for match defined in the regex in rules.yaml file.

3) Gives the output on the basis of findings.

# Features

1) Gives Positive Results<br>
2) Very easy to use and run.<br>
3) Ignore low findings by using --ignore flag<br>
4) Send output file to slack, jira<br>

## How to create your own Rule

This is the common format for any rule you want to create - 

1) `id` this is important to know, when we are creating any rule, the id must be the same as what we are looking inside yaml. In this case id is `image` because we are looking for `image: php:7`. This is case sensitive.

```
-   id: image
    regex: image\s*\:\s+\w+\:\d+
    message: Alert - Image version used instead of latest - Please Check if version is latest
    severity: Low

```

2) `regex` We need to create a simple regex for the flag we wanted to scan. In this case it checks this match `image: php:7`.

## What if creating regex is not Possible?

In many cases, you might find out that regexes is not possible, for ex- scanning RBAC policies, this can be very tricky. In this case we need to follow some steps to scan such kind of configurations.

1) Define the regex for the key we wanted to look into yaml - For ex:

```
rules:
  - apiGroups: [""]
    resources: ["*"]
    verbs: ["*"]
```

In this case we wanted to check for RBAC policies, and these policies have this rules key. we need to add regex for `rules:` which will check if `rules` key is present.

2) Once we added regex, then We need to set additional flag for that rule. for ex - 

```
-   id: rules
    regex: rules\s*\:\s*
    message: None
    severity: None
    scan: true
```

`scan: true` this scan let the scanner to run external scan for the rule.

3) Next we need to create a external function inside `externalscan` file stored in src/yaml folder, the function name must be same as `id` name in rules.yaml file.<br>
4) Next Map the function name inside functions_list in the same `externalscan` file.<br>

```
functions_list = {
    'rules': rules, 
    'allowedCapabilities':allowedCapabilities
    
} 

```
### Requirements

PHP, Python3

If you don't have any of these please download, then,

1) Python V3 must be installed
2) On terminal:- `pip3 install -r requirements.txt`<br> 
3) On terminal:- `python3 scodescanner.py --help`<br>

If still you face import error please try to import it with pip and open a issue if possible.

### Config.json

1) Please give the Slack token and channel name if you used --slack flag<br>
2) Please give username, API, Project ID, InstanceURL if you used --jira flag.<br>


## Give me shout out

If you found anything by the help of ScodeScanner, only thing it wants a Shout Out, that will great. 

## Feedback/Suggestions/Help

It would be really great to me if you give suggestions/improvements. Ping me on twitter at agrawalsmart7. I would love to hear and improve this tool.

## Sample Data

```
{
    "/Users/uagrawal/pentesting/tools/testing/sc5/src/yaml/namespacess.yml": [
        {
            "id": "pod-security.kubernetes.io/enforce",
            "line": "pod-security.kubernetes.io/enforce: privileged",
            "lineno": 6,
            "message": "Alert - Found Enforced High Privileged POD Security Policy",
            "severity": "High"
        }
    ]
}{
    "/Users/uagrawal/pentesting/tools/testing/sc5/src/yaml/role.yml": [
        {
            "id": "rules",
            "line": [
                {
                    "rules:\n  ": [
                        {
                            "apiGroups": [
                                ""
                            ],
                            "resources": [
                                "*"
                            ],
                            "verbs": [
                                "*"
                            ]
                        }
                    ]
                }
            ],
            "lineno": 7,
            "message": "IMPORTANT1: Super Admin Permissions defined",
            "severity": "Critical"
        }
    ]
}{
    "/Users/uagrawal/pentesting/tools/testing/sc5/src/yaml/apache.yml": [
        {
            "id": "nodePort",
            "line": "nodePort: 30101",
            "lineno": 56,
            "message": "Alert - nodePort will allow the application to accessible pubclily.",
            "severity": "Low"
        },
        {
            "id": "rules",
            "line": [
                {
                    "rules:\n  ": [
                        {
                            "apiGroups": [
                                ""
                            ],
                            "resources": [
                                "*"
                            ],
                            "verbs": [
                                "*"
                            ]
                        }
                    ]
                }
            ],
            "lineno": 82,
            "message": "IMPORTANT1: Super Admin Permissions defined",
            "severity": "Critical"
        }
    ]
}{
    "/Users/uagrawal/pentesting/tools/testing/sc5/src/yaml/main.yml": [
        {
            "id": "image",
            "line": "image: php:7",
            "lineno": 29,
            "message": "Alert - Image version used instead of latest - Please Check if version is latest",
            "severity": "Low"
        },
        {
            "id": "automountServiceAccountToken",
            "line": "automountServiceAccountToken: True",
            "lineno": 18,
            "message": "Alert - SA Token is mounted inside POD - Please change it to false if it is not required.",
            "severity": "Low"
        },
        {
            "id": "env",
            "line": "env: \n      - name: MYSQL_ROOT_PASSWORD",
            "lineno": 30,
            "message": "Alert - ENV Variable used - Please use vault instead.",
            "severity": "Medium"
        },
        {
            "id": "privileged",
            "line": "privileged: true",
            "lineno": 19,
            "message": "Alert - Privileged flag found to set True.",
            "severity": "High"
        },
        {
            "id": "allowPrivilegeEscalation",
            "line": "allowPrivilegeEscalation: true",
            "lineno": 20,
            "message": "Alert - Privilege Escalation found to set True.",
            "severity": "Medium"
        },
        {
            "id": "allowedCapabilities",
            "line": [
                {
                    "allowedCapabilities:\n    ": [
                        "*"
                    ]
                }
            ],
            "lineno": 21,
            "message": "Critical Alert: POD contains admin capabilities",
            "severity": "Critical"
        }
    ]
}

```

## Feedback

I would really like to hear your thoughts on this tool. And if you wanted to contribute in this tool please let me know on Twitter [agrawalsmart7](https://twitter.com/agrawalsmart7) or you can send me a Pull request.


## Future Work

For now, I have focused only on PHP, but in future, I will make this scanner for other languages too. Focused languages are:- PHP, ASP, PYTHON JAVA.
Let me know if anyone interested.

Also, I will update this tool regularly to make it more powerful. 
