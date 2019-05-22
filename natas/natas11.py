
import base64,re,requests,natas

USER='natas11'
PASSWORD=natas.get_credential(USER)
URL='http://natas11.natas.labs.overthewire.org/'
DEFAULT_JSON = '{"showpassword":"no","bgcolor":"#ffffff"}'
MY_JSON = '{"showpassword":"yes","bgcolor":"#ffffff"}'

def main():
    b64 = base64.b64encode('%s:%s' % (USER,PASSWORD))
    cookie = get_cookie(b64)
    cookie = base64.b64decode(cookie.replace('%3D','='))
    
    #find key based of xor circular functionality
    key = shorten_key(xor_encrypt(cookie,DEFAULT_JSON))
    print('key found: %s' % key)

    new_cookie = base64.b64encode(xor_encrypt(MY_JSON, key))
   
    response = requests.get (
        URL,
        headers=dict(Authorization='Basic %s' % b64),
        cookies=dict(data=new_cookie)        
    )

    regex = r"natas12 is (\w+)"
    matches = re.finditer(regex,response.content,re.MULTILINE)

    password = None
    for match in matches:
        password = match.group(1)
    
    if password is not None:
        print ('password found: %s' % password)
        print ('adding to credentials....')
        natas.save_credentials('natas12',password)
        print ('done')

def get_cookie(b64):
    response = requests.get (
            URL,
            headers = {
                'Authorization' : 'Basic %s' % b64
            }
    )
    return response.cookies['data']

def xor_encrypt(query,key):
    out = ''
    
    # Iterate through each character
    for i in range (0, len(query)):
        out = out + chr(ord(query[i]) ^ ord(key[i % len(key)]))
    

    return str(out)

def shorten_key(long_key):
    print ('long key: %s' % long_key)
    
    regex = r"(\w+?)\1{1,}"
    matches = re.finditer(regex,long_key,re.MULTILINE)

    key = None
    for match in matches:
        key = match.group(1)

    return key

if __name__=='__main__':
    main()
