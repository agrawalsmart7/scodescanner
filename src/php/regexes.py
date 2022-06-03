reg = r'(?:GET|POST|REQUEST|COOKIE|FILES|SESSION)\[[\'\"][A-Za-z0-9_-]+[\'\"]\]'
reg2 = r'\$this\-\>+:?\w+'
reg3 = r'\$.+getParam\[[\'\"][A-Za-z0-9_-]+[\'\"]\]'


regway = r'(?:\$_'+reg+'|'+reg3+')' # indivisual variables such as $_GET['aa'] or $getParam['bbb']
regex1 = r'\$\w+.\=+.'+regway 
regex1_1 = r'\=+.'+regway
regex3 = r'('+reg2+regex1_1+')' #$this->test = $_GET['aa'] or $getParam['aa']

regex4 = r'isset\(.?\$_'+reg+'.?\).?\?.?\$_'+reg+'.?\:.?\w+'
regex4_1 = r'\$\w+.\=+.?'+regex4
regex4_2 = r'\=+.'+regex4


# regex6 = r'\$\w+.\=+.*[A-Za-z0-9<>?:;\[\\\]\{\}!@#$%^&*()_`=-]' # for sensitive variables


