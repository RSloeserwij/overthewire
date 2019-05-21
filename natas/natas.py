
CRED_FILE = 'credentials'

def get_credentials():
    credentials = {}
    f = open(CRED_FILE, 'r+')
    for line in f:
        k = line.split('\t')[0]
        v = line.split('\t')[1].replace('\n','')
        credentials[k] = v
    f.close()
    return credentials 

def get_credential(key):
    return get_credentials()[key]

def save_credentials (key, val):
    credentials = get_credentials()
    credentials[key] = val
    f = open(CRED_FILE, 'w')
    for k in credentials:
        f.write('%s\t%s\n' % (k,credentials[k]))



        
    

