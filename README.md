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

## How does it work?

1) There are number of yaml files inside rules directory those yaml files contains `$replace` which actually replaced with php variable for ex: `$uservar, $_GET['aaa']`. 

2) The variables are grepped by Regex and get replace the variables defined inside yaml files ($replace) and creates new yaml file inside `/temp` directory. 

3) Then this tool runs semgrep and use the temp directory as config path and start scanning the code.

## Semgrep Errors you should know?

1) There are some errors you might face when running the tool - 

`Error while running rules: 'utf-8' codec can't decode byte 0xe2 in position 3622: invalid continuation byte` <br>This means that some of your file is not PHP even if the extension is `.php`, so you need proper formated of PHP files (which of-course modern IDE also alerts you)

2) If you face any error related to this:-

`Error while running rules: Separator is not found, and chunk exceed the limit`

Again its semgrep error, and it generate because of running huge number of rules on huge number of files - 

## Want to Create Rules?

There are two types of rules you can create and those are differ by their file name -
1) all_rule_something.yaml
2) rule_something.yaml

The difference between in these yaml files is the `all` naming files scans the whole source code without the use of userinput variable. It does not support any user defined variable, it just scan the pattern and if pattern match inside any file it returns the result.

For ex:- 

```
$Y = $SYSFUNC[...];
...
$Z = "...$Y...";
...
echo $Z;
```

This above pattern will find this XSS -

```
 $pin = $_POST['pin'];

if (!is_numeric($pin) || (strlen($pin) != 3)) {
  $message = "Sorry, the pin '$pin' is Invalid";
  echo $message;
  }
  
```

For the second one, write the semgrep rule and use `$replace` variable where ever you want to change with actual variable. 

**Note**: We used $replace inside ruleID and message in yaml, that will make the file different for each variable.

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
