import re


with open("uploads/final/testing.php", 'r', encoding="UTF-8") as f:

    content = [line.strip() for line in f.readlines()]
    string = "$test"
    pre_variables =re.escape(string)
    print(pre_variables)
    loc_regex = r'(?:\w+\([^()]*|\w+\(\w+\(*)'+pre_variables+r'[^()]*\)'

    print(re.findall(loc_regex, content))
    