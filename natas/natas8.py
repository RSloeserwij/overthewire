
import re,requests,natas,base64,binascii

USER='natas8'
PASSWORD=natas.get_credential(USER)

URL='http://natas8.natas.labs.overthewire.org'

def main():
    b64 = base64.b64encode('%s:%s' % (USER,PASSWORD))
    e_secret = get_encoded_secret(b64)
    secret = decode_secret(e_secret)

    response = requests.post (
            URL,
            headers = {
                'Authorization':'Basic %s' % b64
            },
            data = {
                'secret':secret,
                'submit':'Submit+Query'
            }
    )
    regex = r"The password for natas9 is (\w+)"
    matches = re.finditer(regex,response.content,re.MULTILINE)

    password = None
    for match in matches:
        password = match.group(1)

    if password is not None:
        print('found password: %s' % password)
        print('adding password to credentials....')
        natas.save_credentials('natas9',password)
        print('done')
    

def get_encoded_secret(b64):
    response = requests.get(
            '%s%s' % (URL,'/index-source.html'),
            headers = {
                'Authorization': 'Basic %s' % b64
            }
    )
    regex = r"\$encodedSecret&nbsp;=&nbsp;\"(\w+)\";"
    matches = re.finditer(regex, response.content, re.MULTILINE)
    for match in matches:
        return match.group(1)

def decode_secret(e_secret):
    b_secret = binascii.unhexlify(e_secret)
    r_secret = ''
    for char in b_secret:
        r_secret = char + r_secret
    return base64.b64decode(r_secret)

if __name__=='__main__':
    main()
