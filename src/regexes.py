var = r'(?:\"|\'|\s\"|\s\')[a-zA-Z0-9+(?:\"|\'|\s\"|\s\')]+'

reg = r'(?:GET|POST|REQUEST|COOKIE|FILES)\['+var+'\]'
reg2 = r'\$this((\-\>)+(:?[a-zA-Z]|[a-zA-Z\(\)])+)+'
reg3 = r'\$.+getParam\('+var+'\)'
reg4 = r'\$[a-zA-Z]\['+var+'\]'
reg5 = r''

# reg4 = r'somehitn'


regway = r'(?:\$_'+reg+'|'+reg3+')'

regex1 = r'\$\w+.\=+.'+regway 
regex1_1 = r'\=+.'+regway
regex2 = regway
regex3 = r'(?:echo|print|print_r)+.'+regway
regex4 = r'(?:\.|\.+\s|echo+\s|echo|print+\s|print|print+\s+print_r)+'+regway # for $_GET["AA"] with white space
regex5 = r'(?:\.|\.+\s|echo+\s|echo|print+\s|print|print_r+\s+print_r)' 
# regex7 = r'\$\w+.\=+'+reg3

regex6 = r'\$\w+.\=+.*[A-Za-z0-9<>?:;\[\\\]\{\}!@#$%^&*()_`=-]' # for sensitive variables


# Below are the needs 

# $request->getparam('password') Not sure

# $parts = parse_url($url);
# parse_str($parts['query'], $query);
# echo $query['email'];

# $x = $this->getRequest()->getParam('id'); $this->auth->user()->id

# echo info($img);