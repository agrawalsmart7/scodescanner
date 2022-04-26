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
8) Send file to Jira
9) Send file to Slack
10) Added False Positive Remover

## How does it work?

1) There are number of yaml files inside rules directory those yaml files contains `$replace` which actually replaced with php variable for ex: `$uservar, $_GET['aaa']`. 

2) The variables are grepped by Regex and get replace the variables defined inside yaml files ($replace) and creates new yaml file inside `/temp` directory. 

3) Then this tool runs semgrep and use the temp directory as config path and start scanning the code.

## Semgrep Errors you should know?

1) There are some errors you might face when running the tool - <br><br>`Error while running rules: 'utf-8' codec can't decode byte 0xe2 in position 3622: invalid continuation byte` <br><br>This means that some of your file is not PHP even if the extension is `.php`, so you need proper formated of PHP files (which of-course modern IDE also alerts you)

2) If you face any error related to this:-<br><br>`Error while running rules: Separator is not found, and chunk exceed the limit` <br><br>Again its semgrep error, and it generate because of running huge number of rules on huge number of files - 

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

### Config.json

1) Please give the Slack token and channel name if you used --slack flag<br>
2) Please give username, API, Project ID, InstanceURL if you used --jira flag.<br>


## Give me shout out

If you found anything by the help of ScodeScanner, only thing it wants a Shout Out, that will great. 

## Sample Data

```
uploads/PHP-Multi-Cloud-School-Management-/application/models/Parents_model.php 
     temp.Rule-SQLi-$school_id
        Possible SQL Injection for variable -  $school_id


        171┆  ... $school_id."' AND status='paid';"; ... [0m
[Shortened a long line from output, adjust with --max-chars-per-line]
          ⋮┆----------------------------------------
        180┆  ... $school_id."' AND status='paid';"; ... [0m
[Shortened a long line from output, adjust with --max-chars-per-line]
          ⋮┆----------------------------------------
        189┆  ... $school_id."';"; ... [0m
[Shortened a long line from output, adjust with --max-chars-per-line]
          ⋮┆----------------------------------------
        198┆ $myquery = "SELECT * FROM students_payment WHERE session = '".$session."' AND student_id ='".$child['student_id']."' AND school_id='".$school_id."';";


 uploads/PHP-Multi-Cloud-School-Management-/application/views/public/contact_view.php 
     temp.Rule-XSS-$_SESSION["action_status_report"]
        XSS Injection -- $_SESSION["action_status_report"]


         18┆ echo $_SESSION['action_status_report'];
          ⋮┆----------------------------------------
     temp.Rule-XSS-$_SESSION['action_status_report']
        XSS Injection -- $_SESSION['action_status_report']


         18┆ echo $_SESSION['action_status_report'];


 uploads/PHP-Multi-Cloud-School-Management-/application/views/public/login_view.php 
     temp.Rule-XSS-$_SESSION['err_msg']
        XSS Injection -- $_SESSION['err_msg']


         14┆ echo $_SESSION['err_msg'];


 uploads/PHP-Multi-Cloud-School-Management-/application/views/public/pre_payment_gateway_view.php 
     temp.Rule-XSS-$ref
        XSS Injection -- $ref


         52┆ echo $ref;


 uploads/PHP-Multi-Cloud-School-Management-/system/libraries/Cache/drivers/Cache_redis.php 
     temp.Rule-unserialize-$value
        Found unserialize Injection for variable -  $value


        158┆ return unserialize($value);


 uploads/complete-php7-ecom-website/addtowishlist.php 
     temp.Rule-XSS-$pid
        XSS Injection -- $pid


         42┆ echo $sql = "INSERT INTO `wishlist` (`pid`, `uid`) VALUES ('$pid', '$uid')";
          ⋮┆----------------------------------------
     temp.Rule-XSS-$uid
        XSS Injection -- $uid


         42┆ echo $sql = "INSERT INTO `wishlist` (`pid`, `uid`) VALUES ('$pid', '$uid')";


 uploads/complete-php7-ecom-website/admin/delcategory.php 
     temp.Rule-SQLi-$id
        Possible SQL Injection for variable -  $id


         10┆ $sql = "DELETE FROM category WHERE id='$id'";


 uploads/complete-php7-ecom-website/admin/delprodimg.php 
     temp.Rule-SQLi-$id
        Possible SQL Injection for variable -  $id


         10┆ $sql = "SELECT thumb FROM products WHERE id=$id";


 uploads/complete-php7-ecom-website/admin/delproduct.php 
     temp.Rule-SQLi-$id
        Possible SQL Injection for variable -  $id


         10┆ $sql = "SELECT thumb FROM products WHERE id=$id";


 uploads/complete-php7-ecom-website/admin/editcategory.php 
     temp.Rule-SQLi-$id
        Possible SQL Injection for variable -  $id


         42┆ $sql = "SELECT * FROM category WHERE id=$id";
          ⋮┆----------------------------------------
     temp.Rule-XSS-$_GET['id']
        XSS Injection -- $_GET['id']


         46┆ <input type="hidden" name="id" value="<?php echo $_GET['id']; ?>">


 uploads/complete-php7-ecom-website/admin/editproduct.php 
     temp.Rule-SQLi-$id
        Possible SQL Injection for variable -  $id


         70┆ $sql = "SELECT * FROM products WHERE id=$id";


 uploads/complete-php7-ecom-website/admin/login.php 
     temp.Rule-SQLi-$password
        Possible SQL Injection for variable -  $password


         34┆ $sql = "SELECT * FROM `admin` WHERE `email`='$email' AND `password`='$password'";


 uploads/complete-php7-ecom-website/admin/order-process.php 
     temp.Rule-SQLi-$oid
        Possible SQL Injection for variable -  $oid


         64┆ $ordsql = "SELECT * FROM orders WHERE id='$oid'";
          ⋮┆----------------------------------------
     temp.Rule-XSS-$_GET['id']
        XSS Injection -- $_GET['id']


        103┆ <input type="hidden" name="orderid" value="<?php echo $_GET['id']; ?>">
          ⋮┆----------------------------------------
     temp.Rule-XSS-$id
        XSS Injection -- $id


         21┆ echo $ordprcsql = "INSERT INTO ordertracking (orderid, status, message) VALUES ('$id', '$status', '$message')";


 uploads/complete-php7-ecom-website/cancel-order.php 
     temp.Rule-SQLi-$oid
        Possible SQL Injection for variable -  $oid


        104┆ $ordsql = "SELECT * FROM orders WHERE id='$oid'";
          ⋮┆----------------------------------------
     temp.Rule-SQLi-$uid
        Possible SQL Injection for variable -  $uid


         66┆ $sql = "SELECT * FROM usersmeta WHERE uid=$uid";
          ⋮┆----------------------------------------
     temp.Rule-XSS-$_GET['id']
        XSS Injection -- $_GET['id']


        137┆ <input type="hidden" name="orderid" value="<?php echo $_GET['id']; ?>">


 uploads/complete-php7-ecom-website/checkout.php 
     temp.Rule-SQLi-$uid
        Possible SQL Injection for variable -  $uid


         50┆ $userSql = "SELECT * FROM `usersmeta` WHERE `uid`='$uid'";


 uploads/complete-php7-ecom-website/delwishlist.php 
     temp.Rule-XSS-$id
        XSS Injection -- $id


         41┆ echo $sql = "DELETE FROM wishlist WHERE id=$id";


 uploads/complete-php7-ecom-website/inc/nav.php 
     temp.Rule-XSS-$cart
        XSS Injection -- $cart


         42┆ echo "<em>" . count($cart) . "</em>";


 uploads/complete-php7-ecom-website/single.php 
     temp.Rule-SQLi-$id
        Possible SQL Injection for variable -  $id


        195┆ $chkrevsql = "SELECT count(*) `reviewcount` FROM `reviews` `r` WHERE r.uid='$uid' AND r.pid='$id'";
          ⋮┆----------------------------------------
     temp.Rule-SQLi-$uid
        Possible SQL Injection for variable -  $uid


        195┆ $chkrevsql = "SELECT count(*) `reviewcount` FROM `reviews` `r` WHERE r.uid='$uid' AND r.pid='$id'";


 uploads/complete-php7-ecom-website/view-order.php 
     temp.Rule-XSS-$oid
        XSS Injection -- $oid


         76┆ <h2>Order #<?php echo $oid; ?></h2>


 uploads/complete-php7-ecom-website/wishlist.php 
     temp.Rule-SQLi-$uid
        Possible SQL Injection for variable -  $uid


         75┆ $wishsql = "SELECT p.name, p.price, p.id AS pid, w.id AS id, w.`timestamp` FROM wishlist w JOIN products p WHERE w.pid=p.id AND w.uid='$uid'";

```

## Feedback

I would really like to hear your thoughts on this tool. And if you wanted to contribute in this tool please let me know on Twitter [agrawalsmart7](https://twitter.com/agrawalsmart7) or you can send me a Pull request.


## Future Work

For now, I have focused only on PHP, but in future, I will make this scanner for other languages too. Focused languages are:- PHP, ASP, PYTHON JAVA.
Let me know if anyone interested.

Also, I will update this tool regularly to make it more powerful. 
