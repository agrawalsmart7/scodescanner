# SCodeScanner

The SCodeScanner stands for Source Code Scanner, where you can scan your source code files like PHP and get identify the vulnerabilities inside it. The tool can use by Pentester, Developer to quickly identify the weakness.

The tool supports the semgrep integration.

Learn more on [http://scodescanner.info](http://scodescanner.info)

## Features

New features are added on this tool.

1) Scans folder inside folder inside folder and so on..
2) Added more ways of finding user controlled variable, one eg:- `$x = $this->getRequest()->getParam('id')`
3) Integration of Semgrep
4) It will not only notify you at which file but also which line the vulnerable code exists for quickly identified it.
5) Results out in `.txt` file
6) Scan each variable in each file
7) Gives you the best results on the basis of rules defined in rules directory.

## How to run it?

### Requirements

PHP, Python3

If you don't have any of these please download, then,

1) Python V3 must be installed
2) On terminal:- `pip3 install -r requirements.txt`<br> 
3) On terminal:- `python3 scodescanner.py --help`<br>

If still you face import error please try to import it with pip and open a issue if possible.

## Feedback

I would really like to hear your thoughts on this tool. And if you wanted to contribute in this tool please let me know on Twitter [agrawalsmart7](https://twitter.com/agrawalsmart7) or you can send me a Pull request.


## Future Work

For now, I have focused only on PHP, but in future, I will make this scanner for other languages too. Focused languages are:- PHP, ASP, PYTHON JAVA.
Let me know if anyone interested.

Also, I will update this tool regularly to make it more powerful. 
