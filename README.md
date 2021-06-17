# SCodeScanner

The SCodeScanner stands for Source Code Scanner, where you can scan your source code files like PHP and get identify the vulnerabilities inside it. The tool can use by Pentester, Developer to quickly identify the weakness.

Learn more on [http://scodescanner.info](http://scodescanner.info)

## New Features

New features are added on this tool.

1) Scans folder inside folder inside folder and so on..
2) Added more functions on which user untrusted input should not allowed
3) Added more ways of finding user controlled variable, one eg:- `$x = $this->getRequest()->getParam('id')` (More to come)
4) Added scan timer ( Scans 4k+ files in 1min around.)
5) Changes in the output results. (Opens a Python HTTP Web server)
6) Provide either Folder or PHP File location.


## Features

The main features for this tool are:-

1) Scans the whole folder which contains multiple PHP files. (Updated, above)
2) Scans folder inside a folder, *NOTE: This scans only one time, it will not scan folders inside folders inside folder* (Supports now, above)
3) It will not only notify you at which file but also which line the vulnerable code exists for quickly identified it.
4) Scans not only the PRE-Defined PHP variables but also scans the custom variables. Like a `$test1 = $_GET["aaa"]`, then it scans for both `$test1` and the `GET` variables inside the source code
5) Scans functions with a function that contains our variable. Like `include(htmlentities($test))` so it will parse this and give the results like the $test variable found inside the include function. Because there might be possiblity of using base64 function instead of htmlentities.
6) Give results out for each file inside the anchors tag (So you can move on to it.)
7) You can add more functions which are dangerous if you found missing any inside the vulnerablefunctions python file.

## Test Vulnerable Folders

This tool uses vulnerable scripts from this repo:- https://github.com/snoopysecurity/Vulnerable-Code-Snippets

There are predifined folder named final, where it contains the PHP files/folder. Just for test. You can also use that folder to see how this tool will find the results in PHP.

On terminal: `python scscanner.py --help`<br>

`--fo - Full path of Foldername`<br>
`--De - If folder inside the uploads directory`<br>
`--fi - Full path for the file`<br>

## Demo Video

Please go to:- http://scodescanner.info/2021/05/21/example-content/

## How to run it?

### Requirements

PHP, Python3

If you don't have any of these please download, then,

1) Python V3 must be installed
2) On terminal:- `pip install -r requirements.txt`<br> 
3) On terminal:- `python scodescanner.py --help`<br>

## Feedback

I would really like to hear your thoughts on this tool. And if you wanted to contribute in this tool please let me know on Twitter [agrawalsmart7](https://twitter.com/agrawalsmart7) or you can send me a Pull request.


## Future Work

For now, I have focused only on PHP, but in future, I will make this scanner for other languages too. Focused languages are:- PHP, ASP, PYTHON JAVA.
Let me know if anyone interested.

Also, I will update this tool regularly to make it more powerful. 
