reg = r'(?:GET|POST|REQUEST|COOKIE|FILES)\[(?:\"|\'|\s\"|\s\')[a-zA-Z0-9+(?:\"|\'|\s\"|\s\')]+\]'

regex1 = r'\$\w+.\=+.\$_'+reg
regex1_1 = r'\=+.\$_'+reg
regex2 = r'\$_'+reg
regex3 = r'(?:echo|print|print_r)+.\$_'+reg
regex4 = r'(?:\.|\.+\s|echo+\s|echo|print+\s|print|print+\s+print_r)+\$_'+reg # for $_GET["AA"] with white space
regex5 = r'(?:\.|\.+\s|echo+\s|echo|print+\s|print|print_r+\s+print_r)' 


