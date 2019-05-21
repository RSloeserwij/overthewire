import requests
import natas
import base64
import re

URL='http://natas0.natas.labs.overthewire.org'

def main():
    usr = 'natas0'
    password = natas.get_credential(usr)
    b64 = base64.b64encode('%s:%s' % (usr,password))
    
    response = requests.get (
            URL,
            headers = {
                'Authorization': 'Basic %s' % b64
            }
    )

    regex = r"<!--The password for natas1 is (\w*?) -->"
    matches = re.finditer(regex,response.content, re.MULTILINE)
    for matchNum, match in enumerate(matches, start=1):
        found_password = match.group(1)
        break

    print('found password: %s' % found_password)
    print('adding to credentials file....')
    natas.save_credentials('natas1',found_password)
    print('done')

    print('DEBUG: credentials - %s' % natas.get_credentials())

if __name__=='__main__':
    main()
