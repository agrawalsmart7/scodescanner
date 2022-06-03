import json
import os

def outresult(outfile, data, homedir):

    try:
        os.chdir(homedir)
        with open(outfile, 'w') as e:
            if type(data)==list:
                for result in data:
                    e.write(json.dumps(result, indent=4, sort_keys=True))
            else:
                e.write(json.dumps(data, indent=4, sort_keys=True))

        return True

    except Exception:
        return False