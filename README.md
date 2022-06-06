# SCodeScanner
SCodeScanner stands for Source Code scanner where the user can scans the source code for finding the Critical Vulnerabilities. The main objective for this scanner is to find the vulnerabilities inside the source code before code gets published in Prod.

## Features

1) Supported <a href="https://github.com/agrawalsmart7/scodescanner/tree/main/src/php"> PHP</a> Language<br>
2) Supported <a href="https://github.com/agrawalsmart7/scodescanner/tree/main/src/yaml">YAML</a> Language<br>
3) Pass results to bug tracking services like Jira also Slack (Sending files to group to multiple people at once).<br>
4) Gives results in JSON format, which can easily be used to any other program.
5) Works with Rules. We only need to create some rules which the target rule is not present in php/yaml directory.
6) Rules that can scan advance patterns
  
## Achievements

SCodeScanner received 5 CVEs for finding vulnerabilities in multiple CMS plugins.
  
* CVE-2022-1465
* CVE-2022-1474
* CVE-2022-1527 
* CVE-2022-1532
* CVE-2022-1604

## How to run?

- Download the repository -<br>
- Run `pip3 install -r requirements.txt` <br>
- And run `python3 scscanner.py --help` <br>

## Feedback/Imporvements

I would love to hear your feedback on this tool. Open issues if you found any. And open PR request if you have something.

# Contact

<a href="https://twitter.com/agrawalsmart7">Utkarsh Agrawal</a><br>
<a href="https://smart7.in">Website</a>
