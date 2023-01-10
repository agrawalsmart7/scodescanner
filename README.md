 <img src="/media/index.svg" width=400>

# SCodeScanner
SCodeScanner stands for Source Code scanner where the user can scans the source code for finding the Critical Vulnerabilities. The main objective for this scanner is to find the vulnerabilities inside the source code before code gets published in Prod.

## Features

1) Supported <a href="https://github.com/agrawalsmart7/scodescanner/tree/main/src/php"> PHP</a> Language<br>
2) Supported <a href="https://github.com/agrawalsmart7/scodescanner/tree/main/src/yaml">YAML</a> Language<br>
3) Pass results to bug tracking services like Jira also Slack (Sending files to group to multiple people at once).<br>
4) Gives results in JSON format, which can easily be used to any other program.
5) Works with Rules. We only need to create some rules which the target rule is not present in php/yaml directory.
6) Rules that can scan advance patterns
  
## How to run?

- Download the repository -<br>
- Run `pip3 install -r requirements.txt` <br>
- And run `python3 scscanner.py --help` <br>
- Run with supported lang like `python3 scscanner.py php --help`

## Why Should I use SCodeScanner?

SCodeScanner is a fully open source, command line-based Python tool for identifying vulnerabilities in code. It is designed to be easy to use and provides a number of features that set it apart from other tools, including:

- Fewer false positives: SCodeScanner includes flags that help to eliminate false positives and only report on vulnerabilities that are confirmed to exist.

- Custom semgrep rules: SCodeScanner works with semgrep but creates its own rules, which helps to avoid false positives and time-consuming scans.

- Command line Python based tool: SCodeScanner is a command-line based Python tool that is easy to use for people of all technical backgrounds. While many open source tools for identifying vulnerabilities are GUI-based, SCodeScanner's command-line interface makes it simple to run from the terminal

- Fast scanning: SCodeScanner's rules are designed to check for multiple vulnerabilities at once, which results in fewer files for the rules to process and a faster scanning process overall.

- Visibility - SCodesScanner supported JIRA, SLACK integrations which gives the visibility on the results identified by sending the file to Slack groups or by making the jira Issue.

- Ability to track user input variables: SCodeScanner can identify instances where user input variables are defined in one file but used insecurely in another file.

- Easy-to-read JSON output: SCodeScanner provides results in a JSON format that is easy to read and can be used for further analysis.

## Achievements

SCodeScanner received 5 CVEs for finding vulnerabilities in multiple CMS plugins.
  
* CVE-2022-1465
* CVE-2022-1474
* CVE-2022-1527 
* CVE-2022-1532
* CVE-2022-1604

## References/Tutorials

* https://smart7.in/2022/07/30/Secure-SDLC-Implementation.html
* https://www.kitploit.com/2022/09/scodescanner-stands-for-source-code.html
* https://securityonline.info/scodescanner-scan-the-source-code-for-finding-the-critical-vulnerabilities/
* https://www.sifatnotes.com/2022/09/scodescanner-scodescanner-stands-for.html
* https://www.cyberhacks200.org/post/source-code-scanner-for-finding-critical-vulnerabilities
* https://smart7.in/2022/06/15/How-I-found-5-CVEs.html
* https://haxf4rall.com/2022/08/11/scodescanner-scan-the-source-code-for-finding-the-critical-vulnerabilities/

## Feedback/Imporvements

I would love to hear your feedback on this tool. Open issues if you found any. And open PR request if you have something.

# Contact

<a href="https://twitter.com/agrawalsmart7">Utkarsh Agrawal</a><br>
<a href="https://smart7.in">Website</a>
